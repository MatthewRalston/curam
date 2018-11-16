# README

curam : a utility for system maintenance for Arch Linux

## Install

```bash
yaourt -S curam-git
```


## Build

```bash
git clone https://github.com/MatthewRalston/curam.git
cd curam
makepkg
#namcap PKGBUILD
#namcap curam-x.x.x-x-any.pkg.tar.gz
```

## Documentation

Documentation can be found in `src/man/curam.1` and build with `make docs` in `src` 

### Usage

```bash
curam -h # Display manpage
curam <-t|--task TASK>

```

### Tasks

* news :

Fetches news about Arch Linux packages.

* upgrade :

Begins by updating the mirrorlist and fetching warnings/news since last upgrade. 

Full system upgrade `pacman -Syu` (`yaourt -Syu` if available)

Package library rebuild, remove orphaned/dropped packages.

Display `.pacsave`/`.pacnew` files and paclog's warnings.

* clean :

Pacman cache is cleaned with `paccache -r`, except 3 recent packages versions.

Locate, report, and remove any broken symlinks in the system.

* errors :

The system logs are mined for errors with `journalctl -p 3 -xb`

System daemon launch failures shown with `systemctl --failed`

* backup :

OS, user home, and media rsync backup to `$BACKUP_LOCATION/backups/current`

.tar.gz snapshot of current, saved to `$BACKUP_LOCATION/backups/tarballs`

S3 sync snapshots to `s3://$BUCKET`, using `$DEFAULT_USER`'s `~/.aws/credentials`

Run as root user, preserves permissions of files, and media.

* restore :

Rsync restore of `$BACKUP_LOCATION/backups/current` backup in `--dry-run` mode only

NOTE: This feature is experimental and catastrophic. Always restore manually.

* config :

Print configurations from `etc/curam/`

### Configuration

* $STORAGE :

Defined in `etc/curam/curam.conf`

Primary storage location for a 'current' rsync snapshot and tarballs.

* $EXTERNAL :

Defined in `etc/curam/curam.conf`

An external HDD or location for media and home directory backups.

* $BUCKET :

Defined in `etc/curam/curam.conf`

Destination S3 bucket for tarballs. Omits the `s3://` prefix.

e.g. `STORAGE=my-personal-snapshots` (not `s3://my-personal-snapshots`)

* $DEFAULT_USER :

Defined in `etc/curam/curam.conf`

User to default to and refer to during backup routines.

This user should have AWS credentials defined in `$HOME/.aws/credentials`

* $OS_EXCLUDES :

Defined in `etc/curam/os_excludes.conf` (Remember the trailing \n)

A list of paths to pass to `rsync` with `--exclude=...`

These are OS path components to exclude from the operating system backup.

Good choices are personal directories, media libraries, and large datasets

* $HOME_EXCLUDES :

Defined in `etc/curam/home_excludes.conf` (Remember the trailing \n)

A list of path components to exclude from the home directory backup.

Good choices are subdirectories in `~/.cache`, `~/.config`, etc.

* $MEDIA_EXCLUDES :

Defined in `etc/curam/media_excludes.conf` (Remember the trailing \n)

A list of path components to exclude from media directory backup.

No defaults. Depends on your organization of your media library.

* $SYMLINKS_CHECK :

Defined in `etc/curam/symlinks_check.conf` (Remember the trailing \n)

A list of directories to recur into while searching for broken symlinks.




## LICENSE

    This file is part of curam

    curam is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    curam is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with curam.  If not, see <https://www.gnu.org/licenses/>.

## Credits

  Michael Dobachesky provided the original concept for Arch maintenance in his 'maint' package on AUR. His script `archNews.py` is used for AUR/Pacman warnings in this package.
  Thanks for the inspiration Michael.
  
## Contributing Guidelines

Thanks for taking the time to contribute!

The following is a set of guidelines for contributing to curam. These are just guidelines, not rules, so use your best judgement and feel free to propose changes to this document in a pull request.

### Getting Started

The application is essentially a shell script with embedded Perl 'Plain Old Documentation' (POD). This repostiroy is formatted as an AUR package for Arch Linux.

See the Arch Wiki on package building if you have not done so already. 

### Issues

Ensure the bug was not already reported by searching on GitHub under issues. If you're unable to find an open issue addressing the bug, open a new issue.

Write detailed information

Detailed information is very helpful to understand an issue.

For example:

How to reproduce the issue, step-by-step.
The expected behavior (or what is wrong).
The application version.
The operating system.

### Pull Requests

Pull Requests are always welcome.
