import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(name="CRunner",
				 options={"build_exe":{"packages":["pygame"],
				 			"include_files":["MPfondo.jpg","pantallaNegro.jpg", "menuPantalla.png",
				 			"obstaculo1.png", "obstaculo2.png", "obstaculo3.png", "pw1", "pw2", "pw3",
				 			"CHASQUI00.png", "CHASQUI01.png", "CHASQUI02.png", "CHASQUI03.png",
				 			"CHASQUI04.png", "CHASQUI05.png", "CHASQUI06.png", "CHASQUI07.png",
				 			"CHASQUI08.png", "CHASQUI09.png", "CHASQUI10.png", "CHASQUI11.png",
				 			"GOKU00.png", "GOKU01.png", "GOKU02.png", "GOKU03.png", "GOKU04.png",
				 			"GOKU05.png", "GOKU06.png", "GOKU07.png", "GOKU08.png", "GOKU09.png",
				 			"GOKU10.png", "GOKU11.png", "HULK00.png", "HULK01.png", "HULK02.png",
				 			"HULK03.png", "HULK04.png", "HULK05.png", "HULK06.png", "HULK07.png",
				 			"HULK08.png", "HULK09.png", "HULK10.png", "HULK11.png"]}},w

				 description = "CRunner Game",
				 executables = executables
				 )