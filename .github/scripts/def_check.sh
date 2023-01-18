#!/bin/bash

################################################################################

RED=31
GREEN=32

CL_NORM="\e[0m"
CL_RED="\e[0;${RED};49m"
CL_GREEN="\e[0;${GREEN};49m"

################################################################################

main() {
  checkForCRC "$1"
  exit $?
}

checkForCRC() {
  local defs_dir="$1"
  local def_file def_name has_errors

  show ""

  for def_file in $defs_dir/* ; do
    def_name=$(basename "$def_file")
    
    if ! grep -qE '"[a-f0-9]{40}"' "$def_file" ; then
      show "${CL_RED}✖ ${CL_NORM} $def_name"
    else
      show "${CL_GREEN}✔ ${CL_NORM} $def_name"
    fi
  done

  if [[ -n "$has_errors" ]] ; then
    show "Found some def files without CRC data!" $RED
    return 1
  fi

  show ""
  show "Everything is fine, all files contains CRC data!" $GREEN

  return 0
}

show() {
  if [[ -n "$2" && -z "$no_colors" ]] ; then
    echo -e "\e[${2}m${1}\e[0m"
  else
    echo -e "$*"
  fi
}

################################################################################

main "$@"
