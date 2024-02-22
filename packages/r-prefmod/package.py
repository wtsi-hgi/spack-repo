# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrefmod(RPackage):
	"""Utilities to Fit Paired Comparison Models for Preferences

	Generates design matrix for analysing real paired comparisons and derived paired comparison data (Likert type items/ratings or rankings) using a loglinear approach. Fits loglinear Bradley-Terry model (LLBT) exploiting an eliminate feature. Computes pattern models for paired comparisons, rankings, and ratings. Some treatment of missing values (MCAR and MNAR). Fits latent class (mixture) models for paired comparison, rating and ranking patterns using a non-parametric ML approach.
	"""
	
	cran = "prefmod" 

	version("0.8-36", md5="a53ebd0dda6e4fa61e43de7eeb82df1e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-gnm@1.0.0:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
