#!/usr/bin/env python3
""" 9-main """


def insert_school(mongo_collection, **kwargs):
    """New id"""
    return mongo_collection.insert_one(kwargs).inserted_id
