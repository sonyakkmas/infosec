## 4. How permissions affect collaboration and isolation

Linux checks permissions in three classes: owner, group and others. Each user falls into the first class that matches.

**Collaboration** is achieved through groups. Users who need shared access are added to a common group, and the shared directory is assigned to that group with permissions like 2770. Members can then read and write each other's files. The setgid bit makes new files inherit the group, so teammates keep access to everything created there. Permissions like 640 allow finer control, for example letting the group read a file but not modify it.

**Isolation** comes from denying access to everyone outside the owner and group. Users not in the group fall under "others", and with 0 permissions they can't read, write or even list the shared directory. Home directories (750 or 700) and private files (600) keep each user's data separate by default.

Group membership takes effect only after a new login. Removing a user from a group, or deleting the account, immediately cuts off their group-based access.