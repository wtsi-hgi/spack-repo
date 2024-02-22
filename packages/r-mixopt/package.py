# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixopt(RPackage):
	"""Mixed Variable Optimization

	Mixed variable optimization for non-linear functions.
    Can optimize function whose inputs are a combination of continuous,
    ordered, and unordered variables.
	"""
	
	homepage = "https://github.com/CollinErickson/mixopt"
	cran = "mixopt" 

	version("0.1.2", md5="998833923439dd335898774057ec5516")

