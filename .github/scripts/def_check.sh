#!/bin/bash

################################################################################

main() {
  checkForCRC "$1"
  exit $?
}

checkForCRC() {
  local defs_dir="$1"

  grep -rn '"!"' "$defs_dir" | grep -vq "git:"

  if [[ $? -eq 1 ]] ; then
    return 0
  fi

  echo "Found defs without CRC:"
  grep -rn '"!"' "$defs_dir" | grep -v "git:"
  
  return 1
}

################################################################################

main "$@"
