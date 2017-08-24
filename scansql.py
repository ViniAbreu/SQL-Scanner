import requests
import re
from datetime import datetime

# Variaveis cronologicas
now = datetime.now()
dia = str(now.day)
mes = str(now.month)
ano = str(now.year)
hora = str(now.hour)
minut = str(now.minute)
segundo = str(now.second)

# Variaveis de cores
vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'
branco = '\033[37m'
original = '\033[0;0m'
reverso = '\033[2m'    
default = '\033[0m'
banner = '''
			 ____   ___  _       ____ 
			/ ___| / _ \| |     / ___|  ___ __ _ _ __  _ __   ___ _ __ 
			\___ \| | | | |     \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
			 ___) | |_| | |___   ___) | (_| (_| | | | | | | |  __/ |   
			|____/ \__\_\_____| |____/ \___\__,_|_| |_|_| |_|\___|_|   

		 '''
about = '''
					+-----------------------+
					|       SQL Scanner     |
					+-----------------------+
					|   Coder: Sr. Biggs    |
					|   Telegram: @SrBiggs  |
					|      Version: 1.0     |
					|   GitHub: SrBiggs     |
					+-----------------------+
		'''
print(default+banner)
print(ciano+about+"\n")

url = str(input(ciano+"Digite a url que deseja scannear: "+default))
padrao = re.search(r'([\w:/\._-]+\?[\w_-]+=)([\w_-]+)', url)
injecao = padrao.groups()[0]+'\''

try:
	SqlVulns_List = ["mysql_num_rows()", "mysql_fetch_array()", "Error Occurred While Processing Request", "Server Error in '/' Application", "Microsoft OLE DB Provider for ODBC Drivers error", "error in your SQL syntax", "Invalid Querystring","OLE DB Provider for ODBC", "VBScript Runtime", "ADODB.Field", "BOF or EOF", "ADODB.Command", "JET Database", "mysql_fetch_row()","Syntax error", "include()", "mysql_fetch_assoc()", "mysql_fetch_object()", "mysql_numrows()", "GetArray()", "FetchRow()","Input string was not in a correct format", "session_start()", "array_merge()", "preg_match()", "ilesize()", "filesize()", "","SQL Error", "[MySQL][ODBC 5.1 Driver][mysqld-4.1.22-community-nt-log]You have an error in your SQL syntax", "You have an error in your SQL syntax", "mysql_query()", "mysql_fetch_object()", "Query failed:", "Warning include() [function.include]", "mysql_num_rows()", "Database Query Failed", "mysql_fetch_assoc()", "mysql_free_result()", "Query failed (SELECT * FROM WHERE id = )", "num_rows", "Error Executing Database Query","Unclosed quotation mark", "Error Occured While Processing Request", "FetchRows()", "Microsoft JET Database", "ODBC Microsoft Access Driver", "OLE DB Provider for SQL Server", "SQLServer JDBC Driver","Error Executing Database Query", "ORA-01756", "getimagesize()", "unknown()", "mysql_result()", "pg_exec()", "require()","Microsoft JET Database", "ADODB.Recordset", "500 - Internal server error", "Microsoft OLE DB Provider", "Unclosed quotes", "ADODB.Command", "ADODB.Field error", "Microsoft VBScript", "Microsoft OLE DB Provider for SQL Server", "Unclosed quotation mark", "Microsoft OLE DB Provider for Oracle", "Active Server Pages error", "OLE/DB provider returned message", "OLE DB Provider for ODBC", "Unclosed quotation mark after the character string", "SQL Server", "Warning: odbc_","ORA-00921: unexpected end of SQL command", "ORA-01756", "ORA-", "Oracle ODBC", "Oracle Error", "Oracle Driver", "Oracle DB2", "error ORA-", "SQL command not properly ended","DB2 ODBC", "DB2 error", "DB2 Driver","ODBC SQL", "ODBC DB2", "ODBC Driver", "ODBC Error", "ODBC Microsoft Access", "ODBC Oracle", "ODBC Microsoft Access Driver","Warning: pg_", "PostgreSql Error:", "function.pg", "Supplied argument is not a valid PostgreSQL result", "PostgreSQL query failed: ERROR: parser: parse error", ": pg_","Warning: sybase_", "function.sybase", "Sybase result index", "Sybase Error:", "Sybase: Server message:", "sybase_", "ODBC Driver","java.sql.SQLSyntaxErrorException: ORA-", "org.springframework.jdbc.BadSqlGrammarException:", "javax.servlet.ServletException:", "java.lang.NullPointerException","Error Executing Database Query", "SQLServer JDBC Driver", "JDBC SQL", "JDBC Oracle", "JDBC MySQL", "JDBC error", "JDBC Driver","java.io.IOException: InfinityDB","Warning: include", "Fatal error: include", "Warning: require", "Fatal error: require", "ADODB_Exception", "Warning: include", "Warning: require_once", "function.include","Disallowed Parent Path", "function.require", "Warning: main", "Warning: session_start\(\)", "Warning: getimagesize\(\)", "Warning: array_merge\(\)", "Warning: preg_match\(\)","GetArray\(\)", "FetchRow\(\)", "Warning: preg_", "Warning: ociexecute\(\)", "Warning: ocifetchstatement\(\)", "PHP Warning:","Version Information: Microsoft .NET Framework", "Server.Execute Error", "ASP.NET_SessionId", "ASP.NET is configured to show verbose error messages", "BOF or EOF","Unclosed quotation mark", "Error converting data type varchar to numeric","LuaPlayer ERROR:", "CGILua message", "Lua error","Incorrect syntax near", "Fatal error", "Invalid Querystring", "Input string was not in a correct format", "An illegal character has been found in the statement","MariaDB server version for the right syntax"]
	log = open('scan.txt', 'a+')
	req = requests.get(injecao)
	html = req.text

	try:
		for erro in SqlVulns_List:
			if erro in html:
				print(azul+"\n+----------------------------------------------+")
				print(default+"|           Vulnerabilidade encontrada         |")
				print(azul+"+----------------------------------------------+")
				print(default+"\n [+]Site: "+url)
				print(default+" [+]Erro: "+erro)
				print(default+" [+]Metodo: GET\n")
				print(azul+"+----------------------------------------------+")
				log.write(str("log [" + dia + "/" + mes + "/" + ano + "][" + hora + ":" + minut + ":" + segundo + "]"))
				log.write(str(" | Site: "+url+" | Erro: "+erro+"\n"))
				log.clsoe()
	except:
		pass
except:
	print(vermelho+"Ocorreu um erro!")
print(default)
