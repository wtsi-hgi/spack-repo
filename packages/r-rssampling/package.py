# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRssampling(RPackage):
	"""Ranked Set Sampling

	Ranked set sampling (RSS) is introduced as an advanced method for data collection which is substantial for the statistical and methodological analysis in scientific studies by McIntyre (1952) (reprinted in 2005) <doi:10.1198/000313005X54180>. This package introduces the first package  that implements the RSS and its modified versions for sampling. With 'RSSampling', the researchers can sample with basic RSS and the modified versions, namely, Median RSS, Extreme RSS, Percentile RSS, Balanced groups RSS, Double RSS, L-RSS, Truncation-based RSS, Robust extreme RSS. The 'RSSampling' also allows imperfect ranking using an auxiliary variable (concomitant) which is widely used in the real life applications. Applicants can also use this package for parametric and nonparametric inference such as mean, median and variance estimation, regression analysis and some distribution-free tests where the the samples are obtained via basic RSS.
	"""
	
	cran = "RSSampling" 

	version("1.0", md5="fcf4c566066e7ee7c0c6e944e3466a13")

	depends_on("r-learnbayes", type=("build", "run"))
