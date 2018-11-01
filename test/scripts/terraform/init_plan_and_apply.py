#!/usr/bin/env python3

# local
import lib.terraform


# =============================================================================
#
# constants
#
# =============================================================================

TEST_WORKING_DIR='test/data/terraform'
TEST_PLAN_FILE_NAME='tfplan'


# =============================================================================
#
# private test functions
#
# =============================================================================

# =============================================================================
# _test__init
# =============================================================================
def _test__init() -> dict:
    lib.terraform.init(working_dir_path=TEST_WORKING_DIR)


# =============================================================================
# _test__plan
# =============================================================================
def _test__plan() -> dict:
    lib.terraform.plan(
        working_dir_path=TEST_WORKING_DIR,
        create_plan_file=True,
        plan_file_name=TEST_PLAN_FILE_NAME)


# =============================================================================
# _test__apply
# =============================================================================
def _test__apply() -> dict:
    lib.terraform.apply(
        working_dir_path=TEST_WORKING_DIR,
        plan_file_name=TEST_PLAN_FILE_NAME)


# =============================================================================
#
# general
#
# =============================================================================

# =============================================================================
# do_test
# =============================================================================
def do_test() -> None:
    _test__init()
    _test__plan()
    _test__apply()


# =============================================================================
#
# main
#
# =============================================================================

if __name__ == "__main__":
    do_test()
