# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVowels(RPackage):
	"""Vowel Manipulation, Normalization, and Plotting

	Procedures for the manipulation, normalization, and plotting of phonetic and sociophonetic vowel formant data.  vowels is the backend for the NORM website.
	"""
	
	homepage = "http://blogs.uoregon.edu/vowels/"
	cran = "vowels" 

	version("1.2-2", md5="6f72947d18a0e36a504a02f2fbebe747")

