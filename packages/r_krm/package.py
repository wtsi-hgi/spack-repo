# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKrm(RPackage):
	"""Kernel Based Regression Models

	Implements several methods for testing the variance component parameter in regression models that contain kernel-based random effects, including a maximum of adjusted scores test. Several kernels are supported, including a profile hidden Markov model mutual information kernel for protein sequence. This package is described in Fong et al. (2015) <DOI:10.1093/biostatistics/kxu056>.
	"""
	
	cran = "krm" 

	version("2022.10-17", md5="c0306e3d0d7c9030adb1c6a9c61a34d4")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-kyotil", type=("build", "run"))
