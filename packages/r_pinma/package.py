# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPinma(RPackage):
	"""Improved Methods for Constructing Prediction Intervals for
Network Meta-Analysis

	Improved methods to construct prediction intervals for network meta-analysis. The parametric bootstrap and Kenward-Roger-type adjustment by Noma et al. (2022) <forthcoming> are implementable.
	"""
	
	cran = "PINMA" 

	version("1.1-2", md5="7b0de0cabfa8f044ea0f18751b85f906")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
