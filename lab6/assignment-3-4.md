## 3. Security vulnerabilities from improper permissions

- **World-writable files (777/666):** any user can modify them. If a world-writable script is run by another user, root or a cron job, an attacker can inject code that runs with those privileges.
- **Readable secrets:** SSH keys, .env files and configs with 644 can be read by every local user. Secrets must be 600.
- **Directory permissions:** removing r doesn't hide files, because with x they can still be accessed by name. w on a shared directory lets users delete or replace others' files unless the sticky bit is set.
- **SUID binaries:** a vulnerable program that runs as root gives a direct path to root.
- **Wrong ownership or excessive groups:** the owner has full control over a file, and groups like sudo or docker are effectively root.

## 4. Permission auditing and least privilege

Least privilege means each user and process gets only the access it needs: 600 for private files, group-based sharing instead of world access, and no unnecessary sudo or group memberships. If an account is compromised, the damage stays limited to that account.

Auditing is needed because permissions drift over time: temporary chmod 777s, leftover group memberships, inactive accounts and reused UIDs. These cause no errors, so they go unnoticed. Regular checks (find -perm -o+w, find -perm -4000, reviewing /etc/group and sudoers) catch them before an attacker does.