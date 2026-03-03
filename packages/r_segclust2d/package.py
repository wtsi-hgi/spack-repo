# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSegclust2d(RPackage):
	"""Bivariate Segmentation/Clustering Methods and Tools

	Provides two methods for segmentation and joint segmentation/clustering of
    bivariate time-series. Originally intended for ecological segmentation
    (home-range and behavioural modes) but easily applied on other series,
    the package also provides tools for analysing outputs from R packages 'moveHMM' and 'marcher'.
    The segmentation method is a bivariate extension of  Lavielle's method available in 'adehabitatLT' 
    (Lavielle, 1999 <doi:10.1016/S0304-4149(99)00023-X> and 2005 <doi:10.1016/j.sigpro.2005.01.012>).
    This method rely on dynamic programming for efficient segmentation.
    The segmentation/clustering method alternates steps of dynamic programming with an Expectation-Maximization algorithm.
    This is an extension of Picard et al (2007) <doi:10.1111/j.1541-0420.2006.00729.x> method 
    (formerly available in 'cghseg' package) to the bivariate case.
    The method is fully described in Patin et al (2018) <doi:10.1101/444794>.
	"""
	
	homepage = "https://github.com/rpatin/segclust2d"
	cran = "segclust2d" 

	version("0.3.1", md5="d0ffb3113528a17483c368688d69369f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-reshape2@1.4.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
