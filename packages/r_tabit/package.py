# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTabit(RPackage):
	"""Simple Tabulation Made Simple

	Simple tabulation should be dead simple. 
    This package is an opinionated approach to easy tabulations while also 
    providing exact numbers and allowing for re-usability. 
    This is achieved by providing tabulations as data.frames with columns for 
    values, optional variable names, frequency counts including and excluding 
    NAs and percentages for counts including and excluding NAs. Also values are
    automatically sorted by in decreasing order of frequency counts to allow for 
    fast skimming of the most important information. 
	"""
	
	cran = "tabit" 

	version("0.2.1", md5="242653bd0044a42a225a22e50a2740e9")

