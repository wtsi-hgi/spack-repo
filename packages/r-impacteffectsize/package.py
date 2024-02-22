# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImpacteffectsize(RPackage):
	"""Calculation and Visualization of the Impact Effect Size Measure

	A non-parametric effect size measure capturing changes in central tendency or shape of data distributions. The package provides the necessary functions to calculate and plot the Impact effect size measure between two groups.
	"""
	
	homepage = "https://cran.r-project.org/package=ImpactEffectsize"
	cran = "ImpactEffectsize" 

	version("0.6.3", md5="5b473014d525258a87c79a725628493d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-paralleldist", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
