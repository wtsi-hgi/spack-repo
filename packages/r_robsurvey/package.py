# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobsurvey(RPackage):
	"""Robust Survey Statistics Estimation

	Robust (outlier-resistant) estimators of finite population
    characteristics like of means, totals, ratios, regression, etc. Available
    methods are M- and GM-estimators of regression, weight reduction,
    trimming, and winsorization. The package extends the 'survey'
    <https://CRAN.R-project.org/package=survey> package.
	"""
	
	homepage = "https://github.com/tobiasschoch/robsurvey"
	cran = "robsurvey" 

	version("0.6", md5="cf706d22ba9c79ff6b2b09dc33cf745e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-survey@3.35.1:", type=("build", "run"))
