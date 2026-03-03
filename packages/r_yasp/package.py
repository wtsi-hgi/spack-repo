# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYasp(RPackage):
	"""String Functions for Compact R Code

	A collection of string functions designed for writing 
    compact and expressive R code. 'yasp' (Yet Another String Package) is simple,
    fast, dependency-free, and written in pure R. The package provides: a
    coherent set of abbreviations for paste() from package 'base' with a
    variety of defaults, such as p() for "paste" and pcc() for "paste and
    collapse with commas"; wrap(), bracket(), and others for wrapping a
    string in flanking characters; unwrap() for removing pairs of characters
    (at any position in a string); and sentence() for cleaning whitespace
    around punctuation and capitalization appropriate for prose sentences.
	"""
	
	homepage = "https://github.com/t-kalinowski/yasp"
	cran = "yasp" 

	version("0.2.0", md5="d24fdc1cd5713138487f0886ed086ee8")

