# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolca(RPackage):
	"""Polytomous Variable Latent Class Analysis

	Latent class analysis and latent class regression models 
    for polytomous outcome variables.  Also known as latent structure analysis.
	"""
	
	homepage = "https://github.com/dlinzer/poLCA"
	cran = "poLCA" 

	version("1.6.0.1", md5="1880d580c0b060ac7708458440462726")

	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
