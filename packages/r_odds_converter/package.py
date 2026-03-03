# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROddsConverter(RPackage):
	"""Betting Odds Conversion

	Conversion between the most common odds types for sports betting.
    Hong Kong odds, US odds, Decimal odds, Indonesian odds, Malaysian odds, and raw
    Probability are covered in this package.
	"""
	
	cran = "odds.converter" 

	version("1.4.8", md5="edd3262c21e6a0aa709f58137132c03b")

