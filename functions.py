def download(url,dest_folder):
    
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    file_name = url.split('/')[-1]
    file_path = os.path.join(dest_folder,file_name)
    
    r = requests.get(url)
    
    if r.ok:
        print(f'Saving file to {file_path}')
        with open(file_path,'wb') as f:
            f.write(r.content)
        f.close()
        
    else: print(f'Failed with code : {r.status_code}')