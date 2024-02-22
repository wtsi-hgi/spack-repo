# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamplingvarest(RPackage):
	"""Sampling Variance Estimation

	Functions to calculate some point estimators and estimate their variance under unequal probability sampling without replacement. Single and two-stage sampling designs are considered. Some approximations for the second-order inclusion probabilities (joint inclusion probabilities) are available (sample and population based). A variety of Jackknife variance estimators are implemented. Almost every function is written in C (compiled) code for faster results. The functions incorporate some performance improvements for faster results with large datasets.
	"""
	
	homepage = "https://www.quantos.mx/"
	cran = "samplingVarEst" 

	version("1.5", md5="d1d2517206962ee6f7ffc102596e3256")

	depends_on("r@3.1:", type=("build", "run"))
