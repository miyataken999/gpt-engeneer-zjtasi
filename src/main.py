from backup import Backup

def main():
    source_dir = "/path/to/source/directory"
    target_dir = "/path/to/target/directory"
    backup = Backup(source_dir, target_dir)

    # Create a backup
    backup.create_backup()

    # List all backups
    backups = backup.list_backups()
    print(backups)

    # Restore a backup
    backup_name = "backup_20230220150000"
    backup.restore_backup(backup_name)

    # Delete a backup
    backup.delete_backup(backup_name)

if __name__ == "__main__":
    main()