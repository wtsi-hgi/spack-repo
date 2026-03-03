# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoundexbr(RPackage):
	"""Phonetic-Coding for Portuguese

	The SoundexBR package provides an algorithm for decoding names
    into phonetic codes, as pronounced in Portuguese. The goal is for
    homophones to be encoded to the same representation so that they can be
    matched despite minor differences in spelling. The algorithm mainly encodes
    consonants; a vowel will not be encoded unless it is the first letter. The
    soundex code resultant consists of a four digits long string composed by
    one letter followed by three numerical digits: the letter is the first
    letter of the name, and the digits encode the remaining consonants.
	"""
	
	cran = "SoundexBR" 

	version("1.2", md5="24deb4e498622bbdf0c06182da300a74")

	depends_on("r@3:", type=("build", "run"))
