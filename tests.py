from functions.get_files_info import get_files_info


def test_get_files_info_dotpath_success():
    response = get_files_info("calculator", ".")
    print(f"Result for current directory:\n{response}")


def test_get_files_info_dir_success():
    response = get_files_info("calculator", "pkg")
    print(f"Result for 'pkg' directory:\n{response}")


def test_get_files_info_oob_abspath_failure():
    response = get_files_info("calculator", "/bin")
    print(f"Result for '/bin' directory:\n{response}")


def test_get_files_info_oob_relpath_failure():
    response = get_files_info("calculator", "../")
    print(f"Result for '../' directory:\n{response}")


def main():
    for func in [
        test_get_files_info_dotpath_success,
        test_get_files_info_dir_success,
        test_get_files_info_oob_abspath_failure,
        test_get_files_info_oob_relpath_failure,
    ]:
        func()


if __name__ == "__main__":
    main()
