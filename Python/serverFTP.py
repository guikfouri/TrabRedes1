
"""Métodos FTP:
         RETRIEVE (RETR) [GET]
            RETR {PATH/ARQUIVO_REMOTO}
            
            This command causes the server-DTP to transfer a copy of the
            file, specified in the pathname, to the server- or user-DTP
            at the other end of the data connection.  The status and
            contents of the file at the server site shall be unaffected.
            

         STORE (STOR) [POST]
            STOR {PATH/ARQUIVO_LOCAL} {PATH_SERVIDOR}

            This command causes the server-DTP to accept the data
            transferred via the data connection and to store the data as
            a file at the server site.  If the file specified in the
            pathname exists at the server site, then its contents shall
            be replaced by the data being transferred.  A new file is
            created at the server site if the file specified in the
            pathname does not already exist.
         
         LIST (LIST) [LS]
            LIST {PATH_SERVIDOR}
            
            This command causes a list to be sent from the server to the
            passive DTP.  If the pathname specifies a directory or other
            group of files, the server should transfer a list of files
            in the specified directory.  If the pathname specifies a
            file then the server should send current information on the
            file.  A null argument implies the user's current working or
            default directory.


         DELETE (DELE) [RM]
            DELE {PATH_SERVIDOR/ARQUIVO_REMOTO}

            This command causes the file specified in the pathname to be
            deleted at the server site.

        Comando que não está no RFC. Fecha a conexão.
        QUIT (QUIT)

        REQUISIÇÃO FTP :
        {COMANDO} {ARGV[1], ARGV[2], ...}

        RESPOSTA:
        {nº do codigo} {codigo}\r\n{dados}


"""

