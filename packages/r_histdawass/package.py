# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHistdawass(RPackage):
	"""Histogram-Valued Data Analysis

	In the framework of Symbolic Data Analysis, a relatively new
    approach to the statistical analysis of multi-valued data, we consider
    histogram-valued data, i.e., data described by univariate histograms. The
    methods and the basic statistics for histogram-valued data are mainly based
    on the L2 Wasserstein metric between distributions, i.e., the Euclidean metric
    between quantile functions. The package contains unsupervised classification
    techniques, least square regression and tools for histogram-valued data and for
    histogram time series. An introducing paper is Irpino A. Verde R. (2015) <doi: 10.1007/s11634-014-0176-4>.
	"""
	
	cran = "HistDAWass" 

	version("1.0.8", md5="db61bbab0f92c83ffdaa2b38b5489bf5")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-histogram", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
