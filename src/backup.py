import os
import shutil
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Backup:
    source_dir: str
    target_dir: str

    def create_backup(self):
        """Create a backup of the source directory in the target directory"""
        backup_dir = os.path.join(self.target_dir, f"backup_{datetime.now().strftime('%Y%m%d%H%M%S')}")
        os.makedirs(backup_dir, exist_ok=True)
        for root, dirs, files in os.walk(self.source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, self.source_dir)
                target_path = os.path.join(backup_dir, rel_path)
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                shutil.copy2(file_path, target_path)

    def list_backups(self):
        """List all available backups in the target directory"""
        backups = [f for f in os.listdir(self.target_dir) if f.startswith("backup_")]
        return backups

    def restore_backup(self, backup_name):
        """Restore a backup from the target directory to the source directory"""
        backup_dir = os.path.join(self.target_dir, backup_name)
        for root, dirs, files in os.walk(backup_dir):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, backup_dir)
                target_path = os.path.join(self.source_dir, rel_path)
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                shutil.copy2(file_path, target_path)

    def delete_backup(self, backup_name):
        """Delete a specific backup from the target directory"""
        backup_dir = os.path.join(self.target_dir, backup_name)
        shutil.rmtree(backup_dir)