# -*- coding: utf-8 -*-
# Copyright 2011-2016 Michael Helmling
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation
#
from __future__ import unicode_literals
import unittest, taglib
from . import copyTestFile


class ID3v2Test(unittest.TestCase):
    
    def test_removeFrame1(self):
        """See https://bugs.kde.org/show_bug.cgi?id=298183
        """
        with copyTestFile('rare_frames.mp3') as f:
            tfile = taglib.File(f)
            self.assertTrue('GENRE' in tfile.tags)
            self.assertEqual(len(tfile.tags['GENRE']), 1)
            del tfile.tags['GENRE']
            tfile.save()
            tfile.close()
            
            tfile = taglib.File(f)
            self.assertTrue('GENRE' not in tfile.tags)
            tfile.close()
            
    def test_removeFrame2(self):
        """See https://bugs.kde.org/show_bug.cgi?id=298183."""
        with copyTestFile('r2.mp3') as f:
            tfile = taglib.File(f)
            self.assertTrue('TITLE' in tfile.tags)
            self.assertEqual(len(tfile.tags['TITLE']), 1)
            del tfile.tags['TITLE']
            tfile.save()
            tfile.close()
            
            tfile = taglib.File(f)
            self.assertTrue('TITLE' not in tfile.tags)
            tfile.close()

    def test_id3v1Tov2(self):
        with copyTestFile('onlyv1.mp3') as f:
            tfile = taglib.File(f)
            self.assertTrue('ARTIST' in tfile.tags)
            self.assertEqual(tfile.tags['ARTIST'][0], 'Bla')
            tfile.tags['NONID3V1'] = ['omg', 'wtf']
            ret = tfile.save()
            self.assertEqual(len(ret), 0)
            tfile.close()
            
            tfile = taglib.File(f)
            self.assertTrue('NONID3V1' in tfile.tags)
            tfile.close()
