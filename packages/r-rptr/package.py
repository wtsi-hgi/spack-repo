# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRptr(RPackage):
	"""Repeatability Estimation for Gaussian and Non-Gaussian Data

	Estimating repeatability (intra-class
    correlation) from Gaussian, binary, proportion and Poisson data.
	"""
	
	cran = "rptR" 

	version("0.9.22", md5="6f908a5e3400d6475d5f1bd2ef3a577a")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
