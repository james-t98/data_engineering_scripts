import pdftables_api
import tabula
file_path = '/Users/jaimetellie/Downloads/2407.07959v1.pdf'
output_path = '/Users/jaimetellie/Documents/University for Artificial Intelligence/data_engineering_scripts/out.pdf'
API_KEY = 'gnsfbqh1ayge'

def main():
    dfs = tabula.read_pdf(file_path,pages=1,lattice=True)

if __name__=='__main__':
    main()