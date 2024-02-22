# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROtsfeatures(RPackage):
	"""Ordinal Time Series Analysis

	An implementation of several functions for feature extraction in 
    ordinal time series datasets. Specifically, some of the features proposed by
    Weiss (2019) <doi:10.1080/01621459.2019.1604370> can be computed.  
    These features can be used to perform inferential tasks or to feed machine
    learning algorithms for ordinal time series, among others. The package also includes some
    interesting datasets containing financial time series. Practitioners from a 
    broad variety of fields could benefit from the general framework provided 
    by 'otsfeatures'.
	"""
	
	cran = "otsfeatures" 

	version("1.0.0", md5="c29738029154b2bdb010c35601d7dbb5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-astsa", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-bolstad2", type=("build", "run"))
