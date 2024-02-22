# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeaksegoptimal(RPackage):
	"""Optimal Segmentation Subject to Up-Down Constraints

	Computes optimal changepoint models using the
 Poisson likelihood for non-negative count data,
 subject to the PeakSeg constraint:
 the first change must be up, second change down, third change up, etc.
 For more info about the models and algorithms,
 read "A log-linear time algorithm for constrained changepoint detection"
 <arXiv:1703.03352> by TD Hocking et al.
	"""
	
	homepage = "https://github.com/tdhock/PeakSegOptimal"
	cran = "PeakSegOptimal" 

	version("2024.1.24", md5="35fbf31263eb4aad53aa9ab9870c8b5b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-penaltylearning", type=("build", "run"))
