from ftplib import FTP
import os

class WalkFTP:
    
    def glob_ftp(self, ftp, store_paths, walk_back=False):
        '''
        Parameters
        ----------
        ftp : obj
            FTP object logged on already
        store_paths : str
            Root directory that you are storing 
            the files
        walk_back : bool
            Leave False. This variable is used for
            navigating folders

        Returns
        -------
        None
        '''
        curr_list = ftp.nlst()

        for f in curr_list:
            if self.test_file(f):
               self.retrieve(store_paths, f, ftp) 
            else:
                new_store_path = os.path.join(store_paths, f)
                ftp.cwd(f)
                self.glob_ftp(ftp, new_store_path, walk_back=True)

        if walk_back: ftp.cwd('../')

    def test_file(self, f):
        '''
        Parameters
        ----------
        f : str
            string of ftp filepath

        Returns
        -------
        bool : whether or note the input is a file (True)
        or a folder (False)
        '''
        if '.' in f:
            # file
            return True
        else:
            # folder
            return False

    def retrieve(self, store_path, f, ftp, blocksize = 8192):
        '''
        Parameters
        ----------
        store_path : str
            Path that you are storing files
        f : str
            File that is the ftp
        ftp: obj
            FTP object already logged on
        blocksize : int
            Rate that you will transfer files

        Returns
        -------
        None
        '''
        if not os.path.exists(store_path):
            os.makedirs(store_path)

        f_store = os.path.join(store_path, f)

        if not os.path.exists(f_store):

            gFile = open(f_store, 'wb')
            print('reading: {}'.format(f))
            ftp.retrbinary('RETR '+f, gFile.write, blocksize=blocksize)
            print('finished writing: {}. Closing...'.format(f_store))
            gFile.close()

    def __init__(self, root, base_url, username, password, store):
        '''
        Parameters
        ----------
        root : str
            root path that you are storing FTP
        base_url : str
            URL that you are pulling the FTP
        username : str
            Username to login to the FTP
        password : str
            Username to login to the FTP
        store : str
            Path after root that you are storing the specific FTP
        '''
        
        output_path = os.path.join(root, store)
        
        ftp = FTP(base_url)
        print(ftp.login(user=username, passwd=password))

        self.glob_ftp(ftp, output_path)
        
        # close ftp
        ftp.close()
