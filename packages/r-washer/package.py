# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWasher(RPackage):
	"""Time Series Outlier Detection

	Time series outlier detection with non parametric test. This is a new outlier detection methodology (washer): efficient for time saving elaboration and implementation procedures, adaptable for general assumptions and for needing very short time series, reliable and effective as involving robust non parametric test. You can find two approaches: single time series (a vector) and grouped time series (a data frame). For other informations: Andrea Venturini (2011) Statistica - Universita di Bologna, Vol.71, pp.329-344. For an informal explanation look at R-bloggers on web.
	"""
	
	cran = "washeR" 

	version("0.1.3", md5="c2e40f55ef09d5b5db307eab7b621424")

	depends_on("r-gplots", type=("build", "run"))
