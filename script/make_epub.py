#! /usr/bin/env python
# -*- coding: utf-8 -*-
#======================================================================
#
# make_epub.py - 
#
# Created by skywind on 2024/05/24
# Last Modified: 2024/05/24 01:38:26
#
#======================================================================
import sys
import time
import os
import gonglue


#----------------------------------------------------------------------
# Epub Book
#----------------------------------------------------------------------
class EpubBook (object):

    def __init__ (self):
        self.htmls = gonglue.list_html()


#----------------------------------------------------------------------
# testing suit
#----------------------------------------------------------------------
if __name__ == '__main__':
    def test1():
        book = EpubBook()
        return 0
    test1()

