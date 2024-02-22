# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParsedate(RPackage):
	"""Recognize and Parse Dates in Various Formats, Including All ISO
8601 Formats

	Parse dates automatically, without the need of
    specifying a format. Currently it includes the git date parser.
    It can also recognize and parse all ISO 8601 formats.
	"""
	
	homepage = "https://github.com/gaborcsardi/parsedate"
	cran = "parsedate" 

	version("1.3.1", md5="94e2cf16a36da1786ee0cba3cd4889e3")

