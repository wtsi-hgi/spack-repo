# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmaExact(RPackage):
	"""Exact Confidence Intervals for Random Effects Meta-Analyses

	Compute an exact CI for the population mean under a random effects model. The routines implement the algorithm described in Michael, Thronton, Xie, and Tian (2017) <https://haben-michael.github.io/research/Exact_Inference_Meta.pdf>.
	"""
	
	cran = "rma.exact" 

	version("0.1.0", md5="c8d639a40b1f9815333507edeb86e033")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
