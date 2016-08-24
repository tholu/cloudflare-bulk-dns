from __future__ import print_function
import os
import sys
import unittest

from CloudFlare.exceptions import CloudFlareAPIError

from cloudflare_dns import CloudFlareLibWrapper


class TestCloudFlareLibWrapper(unittest.TestCase):
    def setUp(self):
        api_key = os.environ.get('CLOUDFLARE_API_KEY')
        api_email = os.environ.get('CLOUDFLARE_API_EMAIL')
        self.lib_wrapper = CloudFlareLibWrapper(api_key, api_email)

    def tearDown(self):
        pass

    def test_create_a_zone(self):
        try:
            zone_info = self.lib_wrapper.create_a_zone('instruct-rustier-adds.press')
            id_key = "id"
            self.assertTrue(id_key in zone_info)
            self.assertNotEqual("", zone_info[id_key].strip())
            print("ZONE INFO:", zone_info.get(id_key), file=sys.stderr)
        except CloudFlareAPIError as e:
            if "already exists" not in e.message:
                raise e


if __name__ == '__main__':
    unittest.main()