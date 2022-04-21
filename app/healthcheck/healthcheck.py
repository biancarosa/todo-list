"""app.healthcheck.healthcheck

Module that deals with HealthCheck route."""
from flask import jsonify
import logging

logger = logging.getLogger(__name__)

def healthcheck():
    """Returns health information"""
    logging.info("Info endpoint hit")
    return jsonify({
        "message": "I feel good."
    })
    