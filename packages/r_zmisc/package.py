# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZmisc(RPackage):
	"""Vector Look-Ups and Safer Sampling

	A collection of utility functions that facilitate looking up
    vector values from a lookup table, annotate values in at table for 
    clearer viewing, and support a safer approach to vector sampling, 
    sequence generation, and aggregation.
	"""
	
	homepage = "https://github.com/torfason/zmisc/"
	cran = "zmisc" 

	version("0.2.3", md5="55f1a7179aae849204826de37bb72b83")

