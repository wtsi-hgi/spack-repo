# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMev(RPackage):
	"""Modelling of Extreme Values

	Various tools for the analysis of univariate, multivariate and functional extremes. Exact simulation from max-stable processes [Dombry, Engelke and Oesting (2016) <doi:10.1093/biomet/asw008>, R-Pareto processes for various parametric models, including Brown-Resnick (Wadsworth and Tawn, 2014, <doi:10.1093/biomet/ast042>) and Extremal Student (Thibaud and Opitz, 2015, <doi:10.1093/biomet/asv045>). Threshold selection methods, including Wadsworth (2016) <doi:10.1080/00401706.2014.998345>, and Northrop and Coleman (2014) <doi:10.1007/s10687-014-0183-z>. Multivariate extreme diagnostics. Estimation and likelihoods for univariate extremes, e.g., Coles (2001) <doi:10.1007/978-1-4471-3675-0>.
	"""
	
	homepage = "https://lbelzile.github.io/mev/"
	cran = "mev" 

	version("1.16", md5="0417a836e93f4948273e042e6e3960bd")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
