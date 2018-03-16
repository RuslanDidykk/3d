# coding=utf-8
from DatabaseModel import Proxy

from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy import update
from sqlalchemy.orm import sessionmaker

class DataBaseManager():
    def __init__(self):
        self.pool_connetcion = self.poolConnect()

    def poolConnect(self):
        engine = create_engine('sqlite://///Programming/Python/Carto.com/database/proxy.db')
        return engine

    def __del__(self):
        print "Disconnected"
        self.pool_connetcion.dispose()

    @contextmanager
    def getConnection(self):
        self.con = self.pool_connetcion.connect()
        DBSession = sessionmaker(bind=self.con)
        session = DBSession()
        try:
            yield session
        finally:
            session.close()
            self.con.close()

    def insertProxies(self, urls_list, session_id, project_id):
        """:param urls_list - {'url': '', 'hash': '', 'proxie': ''}"""
        amount_of_existing = 0
        with self.open_session() as session:
            for url in urls_list:
                url_ = url['url']
                hash = url['hash']
                proxie = url['proxy']
                timestamp = generate_timestamp()
                new_url = Url(url=url_,
                              project_id=project_id,
                              processed=False,
                              hash=hash,
                              session_id=session_id,
                              proxie=proxie,
                              timestamp=timestamp)
                try:
                    session.add(new_url)
                    session.flush()
                    session.commit()
                except Exception as exc:
                    amount_of_existing += 1
                    session.rollback()
        return {'amount_of_existing': amount_of_existing}


    # def selectALl(self):
    #     with self.getConnection() as connection:
    #         try:
    #             data = connection.query(Project).filter(Project.project_id == 1).all()
    #             #возвращает список обьектов
    #
    #             for user in data:
    #                 print user.name
    #         except Exception as e:
    #             print e

# db = DataBaseManager()
# db.insert_urls()
# db.addCar(model='BMW')
# db.updateUser(1,2)
# db.selectALl()