import os
from pathlib import Path
import pytest
import main


# ============================================================
# console_folder_choice
# ============================================================

def test_console_folder_choice_prints_options(capsys):
    main.console_folder_choice()
    out = capsys.readouterr().out
    assert "1: Downloads" in out
    assert "2: Documents" in out
    assert "3. Desktop" in out


# ============================================================
# user_input_folder
# ============================================================

def test_user_input_folder_accepts_valid_choice(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    result = main.user_input_folder()
    assert result == main.DOWNLOAD_PATH


def test_user_input_folder_maps_all_choices(monkeypatch):
    for key, expected in main.p_choices.items():
        monkeypatch.setattr("builtins.input", lambda _, k=key: k)
        assert main.user_input_folder() == expected


def test_user_input_folder_retries_on_invalid_then_accepts(monkeypatch, capsys):
    inputs = iter(["abc", "0", "9", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = main.user_input_folder()
    out = capsys.readouterr().out
    assert result == main.DOCUMENTS_PATH
    assert out.count("Please enter valid index") >= 3


# ============================================================
# user_input_file_extension
# ============================================================

def test_user_input_file_extension(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "pdf")
    assert main.user_input_file_extension() == "pdf"


def test_user_input_file_extension_keeps_case(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "PDF")
    assert main.user_input_file_extension() == "PDF"


# ============================================================
# list_files
# ============================================================

def test_list_files_returns_entries(tmp_path):
    (tmp_path / "a.pdf").write_text("x")
    (tmp_path / "b.txt").write_text("x")
    (tmp_path / "sub").mkdir()

    result = main.list_files(str(tmp_path))

    assert sorted(result) == ["a.pdf", "b.txt", "sub"]


def test_list_files_empty_folder(tmp_path):
    assert main.list_files(str(tmp_path)) == []


def test_list_files_nonexistent_path_returns_empty(tmp_path, capsys):
    missing = tmp_path / "does_not_exist"
    result = main.list_files(str(missing))
    assert result == []


# ============================================================
# create_folder
# ============================================================

def test_create_folder_creates_directory(tmp_path):
    target = main.create_folder(str(tmp_path), "pdf")
    assert target == os.path.join(str(tmp_path), "PDF")
    assert os.path.isdir(target)


def test_create_folder_uppercases_extension(tmp_path):
    target = main.create_folder(str(tmp_path), "docx")
    assert os.path.basename(target) == "DOCX"


def test_create_folder_exist_ok(tmp_path):
    main.create_folder(str(tmp_path), "pdf")
    main.create_folder(str(tmp_path), "pdf")  # darf nicht crashen
    assert os.path.isdir(os.path.join(str(tmp_path), "PDF"))


# ============================================================
# move_files
# ============================================================

def test_move_files_moves_matching_files(tmp_path):
    source = tmp_path / "source"
    target = tmp_path / "target"
    source.mkdir()
    target.mkdir()

    (source / "a.pdf").write_text("x")
    (source / "b.pdf").write_text("x")
    (source / "c.txt").write_text("x")

    files = os.listdir(source)
    main.move_files(files, str(source), str(target), "pdf")

    assert (target / "a.pdf").exists()
    assert (target / "b.pdf").exists()
    assert not (source / "a.pdf").exists()
    assert (source / "c.txt").exists()  # nicht verschoben


def test_move_files_case_insensitive(tmp_path):
    source = tmp_path / "source"
    target = tmp_path / "target"
    source.mkdir()
    target.mkdir()

    (source / "BILD.PDF").write_text("x")
    files = os.listdir(source)
    main.move_files(files, str(source), str(target), "pdf")

    assert (target / "BILD.PDF").exists()


def test_move_files_does_nothing_if_target_missing(tmp_path, capsys):
    source = tmp_path / "source"
    source.mkdir()
    (source / "a.pdf").write_text("x")

    files = os.listdir(source)
    main.move_files(files, str(source), str(tmp_path / "nope"), "pdf")

    assert (source / "a.pdf").exists()
    out = capsys.readouterr().out
    assert "does not exist" in out.lower() or out == ""


def test_move_files_ignores_files_without_extension(tmp_path):
    source = tmp_path / "source"
    target = tmp_path / "target"
    source.mkdir()
    target.mkdir()

    (source / "README").write_text("x")
    (source / "a.pdf").write_text("x")

    files = os.listdir(source)
    main.move_files(files, str(source), str(target), "pdf")

    assert (source / "README").exists()
    assert (target / "a.pdf").exists()