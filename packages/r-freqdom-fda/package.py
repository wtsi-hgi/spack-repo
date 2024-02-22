# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFreqdomFda(RPackage):
	"""Functional Time Series: Dynamic Functional Principal Components

	Implementations of functional dynamic principle components analysis. Related graphic tools and frequency domain methods.
  These methods directly use multivariate dynamic principal components implementation,
  following the guidelines from Hormann, Kidzinski and Hallin (2016), Dynamic Functional Principal Component <doi:10.1111/rssb.12076>.
	"""
	
	cran = "freqdom.fda" 

	version("1.0.1", md5="c75d870fb166284d0315acf63d7ca781")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-freqdom", type=("build", "run"))
