# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInverseregex(RPackage):
	"""Reverse Engineers Regular Expression Patterns for R Objects

	Reverse engineer a regular expression pattern for the characters
    contained in an R object. Individual characters can be categorised into
    digits, letters, punctuation or spaces and encoded into run-lengths. This
    can be used to summarise the structure of a dataset or identify non-standard
    entries. Many non-character inputs such as numeric vectors and data frames
    are supported.
	"""
	
	cran = "inverseRegex" 

	version("0.1.1", md5="e4c1a12415ed82f4634cb8a35a401146")

	depends_on("r@3.5:", type=("build", "run"))
