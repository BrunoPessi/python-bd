import psycopg2
from postgres.conexao import Connection


class Operacoes():

    def salvar_aluno(self, nome, matricula):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            insert = f"""insert into aluno (nome, matricula) values ('{nome}', '{matricula}');"""
            cursor.execute(insert)
            connection.commit()
            print("Aluno inserido com sucesso!")
        except (Exception, psycopg2.DatabaseError) as er:
            print('Error: ', er)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def buscar_aluno(self, aluno):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            buscar = f"""SELECT * from public.aluno where nome = '{aluno}';"""
            cursor.execute(buscar)

            alunos = cursor.fetchall()

            for row in alunos:
                print("\n Aluno encontrado!")
                print("\nId = ", row[0])
                print("nome = ", row[1])
                print("matricula = ", row[2])

        except (Exception, psycopg2.DatabaseError) as er:
            print('Error: ', er)

        finally:
            if connection:
                cursor.close()
                connection.close()

    def remover_aluno(self, aluno):
        try:
            connection = Connection().get_connection()
            cursor = connection.cursor()
            query_delete = f"""delete from aluno where nome = {aluno}"""
            cursor.execute(query_delete)
            connection.commit()
            print('Registro excluído com sucesso!\n')
        except (Exception, psycopg2.DatabaseError) as er:
            print('Error: ', er)
        finally:
            if connection:
                cursor.close()
                connection.close()
