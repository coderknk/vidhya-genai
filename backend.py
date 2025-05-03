# File: tests/test_api_endpoints.py
import requests

BASE_URL = "https://www.analyticsvidhya.com"

def test_homepage_status():
    """Test that the GenAI Pinnacle homepage returns HTTP 200."""
    url = f"{BASE_URL}/genaipinnacle"
    resp = requests.get(url, timeout=10)
    assert resp.status_code == 200
    assert "GenAI Pinnacle Program" in resp.text

def test_terms_endpoint():
    """Test that the Terms of Use page is accessible."""
    url = f"{BASE_URL}/terms"
    resp = requests.get(url, timeout=10)
    assert resp.status_code == 200
    assert "Terms of use" in resp.text

def test_privacy_endpoint():
    """Test that the Privacy Policy page is accessible."""
    url = f"{BASE_URL}/privacy-policy"
    resp = requests.get(url, timeout=10)
    assert resp.status_code == 200
    assert "Privacy policy" in resp.text

def test_nonexistent_page():
    """Test that a non-existent URL returns 404 or redirects."""
    url = f"{BASE_URL}/nonexistent-page"
    resp = requests.get(url, allow_redirects=False)
    # The site might redirect or return 404; accept either as valid behavior
    assert resp.status_code in (301, 302, 404), "Unexpected response code for invalid URL"
