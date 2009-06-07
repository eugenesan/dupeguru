#!/usr/bin/env python
# Unit Name: preferences
# Created By: Virgil Dupras
# Created On: 2009-05-17
# $Id$
# Copyright 2009 Hardcoded Software (http://www.hardcoded.net)

from dupeguru.scanner import (SCAN_TYPE_FILENAME, SCAN_TYPE_FIELDS, SCAN_TYPE_FIELDS_NO_ORDER,
    SCAN_TYPE_TAG, SCAN_TYPE_CONTENT, SCAN_TYPE_CONTENT_AUDIO)

from base.preferences import Preferences as PreferencesBase

class Preferences(PreferencesBase):
    # (width, is_visible)
    COLUMNS_DEFAULT_ATTRS = [ 
        (200, True), # name
        (180, True), # path
        (60, True), # size
        (60, True), # Time
        (50, True), # Bitrate
        (60, False), # Sample Rate
        (40, False), # Kind
        (120, False), # creation
        (120, False), # modification
        (120, False), # Title
        (120, False), # Artist
        (120, False), # Album
        (80, False), # Genre
        (40, False), # Year
        (40, False), # Track Number
        (120, False), # Comment
        (60, True), # match %
        (120, False), # Words Used
        (80, False), # dupe count
    ]
    
    def _load_specific(self, settings, get):
        self.scan_type = get('ScanType', self.scan_type)
        self.word_weighting = get('WordWeighting', self.word_weighting)
        self.match_similar = get('MatchSimilar', self.match_similar)
        self.scan_tag_track = get('ScanTagTrack', self.scan_tag_track)
        self.scan_tag_artist = get('ScanTagArtist', self.scan_tag_artist)
        self.scan_tag_album = get('ScanTagAlbum', self.scan_tag_album)
        self.scan_tag_title = get('ScanTagTitle', self.scan_tag_title)
        self.scan_tag_genre = get('ScanTagGenre', self.scan_tag_genre)
        self.scan_tag_year = get('ScanTagYear', self.scan_tag_year)
    
    def _reset_specific(self):
        self.filter_hardness = 80
        self.scan_type = SCAN_TYPE_TAG
        self.word_weighting = True
        self.match_similar = False
        self.scan_tag_track = False
        self.scan_tag_artist = True
        self.scan_tag_album = True
        self.scan_tag_title = True
        self.scan_tag_genre = False
        self.scan_tag_year = False
    
    def _save_specific(self, settings, set_):
        set_('ScanType', self.scan_type)
        set_('WordWeighting', self.word_weighting)
        set_('MatchSimilar', self.match_similar)
        set_('ScanTagTrack', self.scan_tag_track)
        set_('ScanTagArtist', self.scan_tag_artist)
        set_('ScanTagAlbum', self.scan_tag_album)
        set_('ScanTagTitle', self.scan_tag_title)
        set_('ScanTagGenre', self.scan_tag_genre)
        set_('ScanTagYear', self.scan_tag_year)
    