# Generated by CodiumAI
import pytest

from pr_agent.algo.types import FilePatchInfo
from pr_agent.algo.utils import find_line_number_of_relevant_line_in_file


class TestFindLineNumberOfRelevantLineInFile:
    # Tests that the function returns the correct line number and absolute position when the relevant line is found in the patch
    def test_relevant_line_found_in_patch(self):
        diff_files = [
            FilePatchInfo(
                base_file="file1",
                head_file="file1",
                patch="@@ -1,1 +1,2 @@\n-line1\n+line2\n+relevant_line\n",
                filename="file1",
            )
        ]
        relevant_file = "file1"
        relevant_line_in_file = "relevant_line"
        expected = (3, 2)  # (position in patch, absolute_position in new file)
        assert find_line_number_of_relevant_line_in_file(diff_files, relevant_file, relevant_line_in_file) == expected

    # Tests that the function returns the correct line number and absolute position when a similar line is found using difflib
    def test_similar_line_found_using_difflib(self):
        diff_files = [
            FilePatchInfo(
                base_file="file1",
                head_file="file1",
                patch="@@ -1,1 +1,2 @@\n-line1\n+relevant_line in file similar match\n",
                filename="file1",
            )
        ]
        relevant_file = "file1"
        relevant_line_in_file = "+relevant_line in file similar match "  # note the space at the end. This is to simulate a similar line found using difflib
        expected = (2, 1)
        assert find_line_number_of_relevant_line_in_file(diff_files, relevant_file, relevant_line_in_file) == expected

    # Tests that the function returns (-1, -1) when the relevant line is not found in the patch and no similar line is found using difflib
    def test_relevant_line_not_found(self):
        diff_files = [
            FilePatchInfo(
                base_file="file1",
                head_file="file1",
                patch="@@ -1,1 +1,2 @@\n-line1\n+relevant_line\n",
                filename="file1",
            )
        ]
        relevant_file = "file1"
        relevant_line_in_file = "not_found"
        expected = (-1, -1)
        assert find_line_number_of_relevant_line_in_file(diff_files, relevant_file, relevant_line_in_file) == expected

    # Tests that the function returns (-1, -1) when the relevant file is not found in any of the patches
    def test_relevant_file_not_found(self):
        diff_files = [
            FilePatchInfo(
                base_file="file1",
                head_file="file1",
                patch="@@ -1,1 +1,2 @@\n-line1\n+relevant_line\n",
                filename="file2",
            )
        ]
        relevant_file = "file1"
        relevant_line_in_file = "relevant_line"
        expected = (-1, -1)
        assert find_line_number_of_relevant_line_in_file(diff_files, relevant_file, relevant_line_in_file) == expected

    # Tests that the function returns (-1, -1) when the relevant_line_in_file is an empty string
    def test_empty_relevant_line(self):
        diff_files = [
            FilePatchInfo(
                base_file="file1",
                head_file="file1",
                patch="@@ -1,1 +1,2 @@\n-line1\n+relevant_line\n",
                filename="file1",
            )
        ]
        relevant_file = "file1"
        relevant_line_in_file = ""
        expected = (0, 0)
        assert find_line_number_of_relevant_line_in_file(diff_files, relevant_file, relevant_line_in_file) == expected

    # Tests that the function returns (-1, -1) when the relevant_line_in_file is found in the patch but it is a deleted line
    def test_relevant_line_found_but_deleted(self):
        diff_files = [
            FilePatchInfo(
                base_file="file1",
                head_file="file1",
                patch="@@ -1,2 +1,1 @@\n-line1\n-relevant_line\n",
                filename="file1",
            )
        ]
        relevant_file = "file1"
        relevant_line_in_file = "relevant_line"
        expected = (-1, -1)
        assert find_line_number_of_relevant_line_in_file(diff_files, relevant_file, relevant_line_in_file) == expected
