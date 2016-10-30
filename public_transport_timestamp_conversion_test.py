import unittest
import public_transport_timestamp_conversion as pt_test
import time

class TestPublicTransportTimestampConversion(unittest.TestCase):

    def test_default(self):
        self.assertEqual(str(pt_test.get_datetime('2016-10-29', '22:59:59',
            'CET')), '2016-10-29 22:59:59+02:00')

    def test_pt_timestamp_on_next_day(self):
        self.assertEqual(str(pt_test.get_datetime('2016-10-28', '27:10:11',
            'CET')), '2016-10-29 03:10:11+02:00')

    def test_to_dst_time(self):
        self.assertEqual(str(pt_test.get_datetime('2016-10-30', '13:05:44',
            'CET')), '2016-10-30 13:05:44+01:00')

    def test_to_dst_time2_epoch(self):
        self.assertEqual(pt_test.get_datetime('2016-10-29', '28:30:40',
            'CET').strftime('%s'), '1477794640')

    # TODO this test works fine when you want epoch or UTC timestamp as result
    # At this moment the code returns 2016-10-30T04:30:40+02:00 instead
    # of 2016-10-30T03:30:40+01:00
    # def test_to_dst_time3(self):
    #     self.assertEqual(pt_test.get_datetime('2016-10-29', '28:30:40',
    #         'CET').isoformat(), '2016-10-30 03:30:40+01:00')

    def test_to_normal_time(self):
        self.assertEqual(str(pt_test.get_datetime('2017-03-26', '13:01:02',
            'CET')), '2017-03-26 13:01:02+02:00')

if __name__ == '__main__':
    unittest.main()
