# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWarn(RPackage):
	"""Weaning Age Reconstruction with Nitrogen Isotope Analysis

	This estimates precise weaning ages
	for a given skeletal population
	by analyzing the stable nitrogen isotope ratios of them.
	Bone collagen turnover rates estimated anew and
	the approximate Bayesian computation (ABC)
	were adopted in this package.
	"""
	
	cran = "WARN" 

	version("1.2-4", md5="6ce48423d5d65b574dff3b184d5bd6c3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
