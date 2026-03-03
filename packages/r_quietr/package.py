# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuietr(RPackage):
	"""Simplify Output Verbosity

	Simplifies output suppression logic in R packages, as it's common
    to develop some form of it in R. 'quietR' intends to simplify that problem 
    and allow a set of simple toggle functions to be used to suppress console 
    output.
	"""
	
	homepage = "https://github.com/thomascjohnson/quietR"
	cran = "quietR" 

	version("0.1.0", md5="45e148fcc08e164f162176174224c4a0")

