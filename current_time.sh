#!/bin/bash

WORK_END_HOUR=18
WORK_END_MINUTE=0

current_hour=$(date +%H)
current_minute=$(date +%M)

current_total=$((10#$current_hour * 60 + 10#$current_minute))
end_total=$((WORK_END_HOUR * 60 + WORK_END_MINUTE))

remaining=$((end_total - current_total))

echo "Current time: $(date +%H:%M)."

if [ "$remaining" -gt 0 ]; then
    hours=$((remaining / 60))
    minutes=$((remaining % 60))

    echo "Work day ends after $hours hours and $minutes minutes."
else
    echo "Work day has already ended."
fi
