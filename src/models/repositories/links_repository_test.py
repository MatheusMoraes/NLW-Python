import pytest
import uuid
from datetime import datetime, timedelta
from .links_repository import LinksRepository
from src.models.settings.db_connections_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

# @pytest.mark.skip(reason="Interacao com o banco")
def test_registry_email():
  conn = db_connection_handler.get_connection()
  links_repository = LinksRepository(conn)
  
  links_infos = {
      "id": str(uuid.uuid4()),
      "trip_id": trip_id,
      "link": "https://www.testelink.com.br/links",
      "title": "Link da viagem xpto",
  }

  links_repository.registry_link(links_infos)
  
# @pytest.mark.skip(reason="Interacao com o banco")
def test_find_links_from_trip():
  conn = db_connection_handler.get_connection()
  links_repository = LinksRepository(conn)
  
  links = links_repository.find_links_from_trip(trip_id)
  print()
  print(links)
