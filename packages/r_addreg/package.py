# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAddreg(RPackage):
	"""Additive Regression for Discrete Data

	Methods for fitting identity-link GLMs and GAMs to discrete data,
    using EM-type algorithms with more stable convergence properties than standard methods.
	"""
	
	homepage = "https://github.com/mdonoghoe/addreg"
	cran = "addreg" 

	version("3.0", md5="627deafbb446aafedf71596364857a83")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-glm2", type=("build", "run"))
	depends_on("r-turboem", type=("build", "run"))
