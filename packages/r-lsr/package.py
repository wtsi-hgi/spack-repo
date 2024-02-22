# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsr(RPackage):
	"""Companion to "Learning Statistics with R"

	A collection of tools intended to make introductory 
    statistics easier to teach, including wrappers for common 
    hypothesis tests and basic data manipulation. It accompanies 
    Navarro, D. J. (2015). Learning Statistics with R: A Tutorial 
    for Psychology Students and Other Beginners, Version 0.6. 
	"""
	
	homepage = "https://github.com/djnavarro/lsr"
	cran = "lsr" 

	version("0.5.2", md5="2497120c44990369d8a5a0452288c08a")

