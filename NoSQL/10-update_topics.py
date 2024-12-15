#!/usr/bin/env python3
""" 10-main """


def update_topics(mongo_collection, name, topics):
    """mongo collection"""
    mongo_collection.uptade_many({"name": "name"}, {"$set": {"topics", "topics"}})
    