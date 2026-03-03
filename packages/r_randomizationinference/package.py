# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandomizationinference(RPackage):
	"""Flexible Randomization-Based Inference

	Allows the user to conduct randomization-based inference for a wide variety of experimental scenarios. The package leverages a potential outcomes framework to output randomization-based p-values and null intervals for test statistics geared toward any estimands of interest, according to the specified null and alternative hypotheses. Users can define custom randomization schemes so that the randomization distributions are accurate for their experimental settings. The package also creates visualizations of randomization distributions and can test multiple test statistics simultaneously.
	"""
	
	cran = "randomizationInference" 

	version("1.0.4", md5="f08e943a41e8e2ab6435c0f23f894f19")

	depends_on("r-permute@0.7.8:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
