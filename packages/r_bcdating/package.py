# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcdating(RPackage):
	"""Business Cycle Dating and Plotting Tools

	Tools for Dating Business Cycles using Harding-Pagan (Quarterly Bry-Boschan) method and various plotting features.
	"""
	
	cran = "BCDating" 

	version("0.9.8", md5="41fb5e96da157df77d6f520d01d6bacb")

