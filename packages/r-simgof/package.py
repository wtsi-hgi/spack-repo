# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimgof(RPackage):
	"""Simultaneous Goodness-of-Fits Tests

	Routine that allows the user to run several goodness-of-fit tests.  
    It also combines the tests and returns a properly adjusted family-wise p value.
    Details can be found in <arXiv:2007.04727>.   
	"""
	
	cran = "simgof" 

	version("1.0.2", md5="d39739a07960775930f260b802bbf0ff")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ddst", type=("build", "run"))
