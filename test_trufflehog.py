import os


def test_case_01():
    results_01 = os.system("trufflehog filesystem ../../PycharmProjects/pythonProject")
    return results_01


def test_case_02():
    results_02 = os.system("trufflehog filesystem ../../PycharmProjects/trufflehog-tests")
    return results_02


def test_case_03():
    results_03 = os.system("trufflehog filesystem ../../PycharmProjects/trufflehog-tests --json  > output_TC3.json")
    return results_03


def test_case_04():
    results_04 = os.system("trufflehog filesystem ../../PycharmProjects/trufflehog-tests  --results=verified,unknown  --json  > output_TC4.json")
    return results_04


def test_case_05():
    results_05 = os.system("trufflehog filesystem ../../PycharmProjects/trufflehog-tests/config.env  --results=verified,unknown  --json  > output_TC5.json")
    return results_05


def test_case_06():
    results_06 = os.system("trufflehog git https://github.com/KarolodonerPL/trufflehog-tests.git --results=verified,unknown --json > output_TC6.json")
    return results_06


def test_case_07():
    results_07 = os.system("trufflehog filesystem ../../PycharmProjects/trufflehog-tests_not_exiting --json  > output_TC7.json")
    return results_07


def test_case_08():
    results_08 = os.system("docker run --rm -it -v 'C:\\Users\\karol\\.docker' trufflesecurity/trufflehog:latest github --repo https://github.com/KarolodonerPL/trufflehog-tests.git  --json  > output_TC8.json")
    return results_08


if __name__ == '__main__':
    test_case_01()
    test_case_02()
    test_case_03()
    test_case_04()
    test_case_05()
    test_case_06()
    test_case_07()
    test_case_08()
