import requests
from pathlib import Path
import gzip
import shutil
import os

# iterate all rows from txt file and download to folder
# https://ftp.ebi.ac.uk/pub/databases/Rfam/CURRENT/fasta_files/RF03160.fa.gz

def download_rfam_fasta(family_id, output_dir):
    url = f"https://ftp.ebi.ac.uk/pub/databases/Rfam/CURRENT/fasta_files/{family_id}.fa.gz"
    output_gz_path = output_dir / f"{family_id}.fa.gz"
    output_fa_path = output_dir / f"{family_id}.fa"

    try:
        response = requests.get(url, timeout=50)
        response.raise_for_status()

        with open(output_gz_path, 'wb') as f:
            f.write(response.content)
        
        with gzip.open(output_gz_path, 'rb') as f_in:
            with open(output_fa_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        output_gz_path.unlink()
    
    except Exception as e:
        print(f"Failed to download or extract {family_id}: {e}")

def main():
    code_dir = os.path.dirname(os.path.abspath(__file__))
    families_file = os.path.join(code_dir, "rfam-families.txt")
    output_dir = Path("rfam-families-fasta")
    output_dir.mkdir(exist_ok=True)

    families_path = Path(families_file)
    families = [line.strip() for line in families_path.read_text().splitlines() if line.strip()]

    for family_id in families:
        #print(family_id)
        download_rfam_fasta(family_id, output_dir)

if __name__ == "__main__":
    main()
