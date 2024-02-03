#!/bin/bash

set -e

printf "Found files in workspace:\n"
ls

printf "Looking for urlchecker install...\n"
which urlchecker

COMMAND="urlchecker check "

# branch is optional
if [ ! -z "${INPUT_BRANCH}" ]; then
    COMMAND="${COMMAND} --branch ${INPUT_BRANCH}"
fi

# no_check_certs is optional
if [ ! -z "${INPUT_NO_CHECK_CERTS}" ]; then
    COMMAND="${COMMAND} --no-check-certs"
fi

# cleanup is optional (boolean)
if [ "${INPUT_CLEANUP}" == "true" ]; then
    COMMAND="${COMMAND} --cleanup"
fi

# subfolder is optional
if [ ! -z "${INPUT_SUBFOLDER}" ]; then
    COMMAND="${COMMAND} --subfolder ${INPUT_SUBFOLDER}"
fi


# print all defaults to true (unless set to false)
if [ "${INPUT_PRINT_ALL}" == "false" ]; then
    COMMAND="${COMMAND} --no-print"
    echo "Automated PR requested"
fi

# verbose defaults to false
if [ "${INPUT_VERBOSE}" == "true" ]; then
    COMMAND="${COMMAND} --verbose"
fi

# run in serial for debugging?
if [ "${INPUT_SERIAL}" == "true" ]; then
    COMMAND="${COMMAND} --serial"
fi


# Do we have a number of workers defined?
if [ ! -z "${INPUT_WORKERS}" ]; then
    export URLCHECKER_WORKERS=${INPUT_WORKERS}
fi

# file types are optional
if [ ! -z "${INPUT_FILE_TYPES}" ]; then
    COMMAND="${COMMAND} --file-types ${INPUT_FILE_TYPES}"
fi


# exclude (previously whitelisted) urls are optional
if [ ! -z "${INPUT_EXCLUDE_URLS}" ]; then
    COMMAND="${COMMAND} --exclude-urls ${INPUT_EXCLUDE_URLS}"
fi

# exclude (previously white listed) patterns are optional
if [ ! -z "${INPUT_EXCLUDE_PATTERNS}" ]; then
    COMMAND="${COMMAND} --exclude-patterns ${INPUT_EXCLUDE_PATTERNS}"
fi

# exclude (previously white listed) files are optional
if [ ! -z "${INPUT_EXCLUDE_FILES}" ]; then
    COMMAND="${COMMAND} --exclude-files ${INPUT_EXCLUDE_FILES}"
fi


# retry count (optional)
if [ ! -z "${INPUT_RETRY_COUNT}" ]; then
    COMMAND="${COMMAND} --retry-count ${INPUT_RETRY_COUNT}"
fi

# timeout (optional)
if [ ! -z "${INPUT_TIMEOUT}" ]; then
    COMMAND="${COMMAND} --timeout ${INPUT_TIMEOUT}"
fi

# files (optional)
if [ ! -z "${INPUT_INCLUDE_FILES}" ]; then
    COMMAND="${COMMAND} --files ${INPUT_INCLUDE_FILES}"
fi

# save (optional)
if [ ! -z "${INPUT_SAVE}" ]; then
    COMMAND="${COMMAND} --save ${INPUT_SAVE}"
fi

# force pass (optional)
if [ "${INPUT_FORCE_PASS}" == "true" ]; then
    echo "Force pass requested."
    COMMAND="${COMMAND} --force-pass"
fi

# git path, if not defined, we assume $PWD
if [ -z "${INPUT_GIT_PATH}" ]; then
    echo "git_path not set, will use present working directory."
    COMMAND="${COMMAND} ."
else
    echo "git_path set, will use for path or clone."
    COMMAND="${COMMAND} ${INPUT_GIT_PATH}" 
fi

echo "${COMMAND}"

${COMMAND}
echo $?
