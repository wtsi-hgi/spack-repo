# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVardpoor(RPackage):
	"""Variance Estimation for Sample Surveys by the Ultimate Cluster
Method

	Generation of domain variables, linearization of several non-linear population statistics (the ratio of two totals, weighted income percentile, relative median income ratio, at-risk-of-poverty rate, at-risk-of-poverty threshold, Gini coefficient, gender pay gap, the aggregate replacement ratio, the relative median income ratio, median income below at-risk-of-poverty gap, income quintile share ratio, relative median at-risk-of-poverty gap), computation of regression residuals in case of weight calibration, variance estimation of sample surveys by the ultimate cluster method (Hansen, Hurwitz and Madow, Sample Survey Methods And Theory, vol. I: Methods and Applications; vol. II: Theory. 1953, New York: John Wiley and Sons), variance estimation for longitudinal, cross-sectional measures and measures of change for single and multistage stage cluster sampling designs (Berger, Y. G., 2015, <doi:10.1111/rssa.12116>). Several other precision measures are derived - standard error, the coefficient of variation, the margin of error, confidence interval, design effect.
	"""
	
	homepage = "https://csblatvia.github.io/vardpoor/"
	cran = "vardpoor" 

	version("0.20.1", md5="3d7b018fd366ee66741fe1c0e5e29743")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-data-table@1.12.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-surveyplanning", type=("build", "run"))
	depends_on("r-laeken", type=("build", "run"))
