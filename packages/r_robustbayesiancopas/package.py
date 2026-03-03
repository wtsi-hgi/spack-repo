# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustbayesiancopas(RPackage):
	"""Robust Bayesian Copas Selection Model

	Fits the robust Bayesian Copas (RBC) selection model of Bai et al. (2020) <arXiv:2005.02930> for correcting and quantifying publication bias in univariate meta-analysis. Also fits standard random effects meta-analysis and the Copas-like selection model of Ning et al. (2017) <doi:10.1093/biostatistics/kxx004>. 
	"""
	
	cran = "RobustBayesianCopas" 

	version("2.0", md5="947363c67535fd410928db4b8b290c71")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-statip", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
