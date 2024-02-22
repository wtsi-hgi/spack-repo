# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmcat(RPackage):
	"""Generalized Linear Models for Categorical Responses

	In statistical modeling, there is a wide variety of regression models for categorical dependent variables (nominal or ordinal data); yet, there is no software embracing all these models together in a uniform and generalized format. Following the methodology proposed by Peyhardi, Trottier, and Guédon (2015) <doi:10.1093/biomet/asv042>, we introduce 'GLMcat', an R package to estimate generalized linear models implemented under the unified specification (r, F, Z). Where r represents the ratio of probabilities (reference, cumulative, adjacent, or sequential), F the cumulative cdf function for the linkage, and Z, the design matrix.
	"""
	
	homepage = "https://github.com/ylleonv/GLMcat"
	cran = "GLMcat" 

	version("0.2.6", md5="8870da1052531c97bb6b50daa219a30b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ordinal", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
