# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFreq(RPackage):
	"""FREQ: Estimate population size from capture frequencies

	Real capture frequencies will be fitted to various distributions which provide the basis of estimating population sizes, their standard error, and symmetric as well as asymmetric confidence intervalls. 
	"""
	
	cran = "FREQ" 

	version("1.0", md5="c2c000fb15e356b13739aeb71e8a77b1")

