#!/usr/bin/env bash

# Template version: 2022.12.12

# Default shell settings
set -o errexit  # -e: Exit when a command fails
set -o nounset  # -u: Treat unset variables as an error
set -o pipefail #   : The return value of a pipeline is the value of the last command that failed

# Debug options
# set -o noexec   # -n: Read and parse but do not execute commands
# set -o verbose  # -v: Print shell input lines as they are read
# set -o xtrace   # -x: Print commands before execution

# Default variables
readonly local IFS=$'\t\n'  # Split on newlines and tabs (but not on spaces)
readonly local script_name=$(basename "${0}")
readonly local script_dir=$( cd "$( dirname "${BASH_SOURCE[0]:-${(%):-%x}}" )" && pwd )  # https://stackoverflow.com/q/9901210


###############################################################################
# Start or attach tmux session
###############################################################################

main() {
    readonly local sessionname=$(basename "${script_dir}")
    if ! tmux has-session -t "${sessionname}" &> /dev/null
    then
        cd "${script_dir}"

        tmux new-session -s "${sessionname}" -d -n "edit"
        tmux send-keys -t "${sessionname}":edit "vim -S" C-m

        tmux new-window -t "${sessionname}" -d -n "shell"
        tmux send-keys -t "${sessionname}":shell "git status --ignored" C-m
        tmux send-keys -t "${sessionname}":shell "git pull"

        tmux new-window -t "${sessionname}" -d -n "container"
        tmux send-keys -t "${sessionname}":container "container/run.sh"
    fi

    readonly local mode=${1:-'--attach'}
    if [ "${mode}" = '--detach' ]
    then
        return
    fi

    extras "${@}"
    tmux attach -t "${sessionname}"
}


extras() {
    # Setup additional sessions
    # ~/code/ansible/Session.sh --detach
    return
}


main "${@}"
