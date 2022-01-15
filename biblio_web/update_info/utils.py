#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2021 seamus tuohy, <code@seamustuohy.com>
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the included LICENSE file for details.

import biblio
import sqlite3
from os import environ

import logging
logging.basicConfig(level=logging.ERROR)
log = logging.getLogger(__name__)

def get_db_path():
    try:
        dbpath = environ['BiblioDBPath']
    except KeyError as _e:
        log.error("You must set the ENV variable \"BiblioDBPath\" with the path to the biblio database.")
        raise _e

def update_biblio_object(file_path, properties):
    db = sqlite3.connect(get_db_path())
    object_uid = biblio.get_file_id(file_path)
    data = biblio.get_all_data(object_uid, db)
    for key,val in data.items():
        if data['object'].get(key) != properties.get(key):
            biblio.update_object_in_db(db,
                                       object_uid,
                                       key,
                                       val)
    return biblio.get_all_data(object_uid, db)

def get_biblio_object(file_path):
    db = sqlite3.connect(get_db_path())
    object_uid = biblio.get_file_id(file_path)
    data = biblio.get_all_data(object_uid, db)
    return data
