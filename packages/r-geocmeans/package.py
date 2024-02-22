# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeocmeans(RPackage):
	"""Implementing Methods for Spatial Fuzzy Unsupervised
Classification

	Provides functions to apply spatial fuzzy unsupervised classification, visualize and interpret results. This method is well suited when the user wants to analyze data with a fuzzy clustering algorithm and to account for the spatial dimension of the dataset. In addition, indexes for estimating the spatial consistency and classification quality are proposed.
    The methods were originally proposed in the field of brain imagery (seed Cai and al. 2007 <doi:10.1016/j.patcog.2006.07.011> and Zaho and al. 2013 <doi:10.1016/j.dsp.2012.09.016>) and recently applied in geography (see Gelb and Apparicio <doi:10.4000/cybergeo.36414>).
	"""
	
	homepage = "https://github.com/JeremyGelb/geocmeans"
	cran = "geocmeans" 

	version("0.3.4", md5="a14ff3138e28974e08177344775feb69")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-tmap@3.3.1:", type=("build", "run"))
	depends_on("r-spdep@1.1.2:", type=("build", "run"))
	depends_on("r-reldist@1.6.6:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-fclust@2.1.1:", type=("build", "run"))
	depends_on("r-fmsb@0.7:", type=("build", "run"))
	depends_on("r-future-apply@1.4:", type=("build", "run"))
	depends_on("r-progressr@0.4:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-sf@1.0.6:", type=("build", "run"))
	depends_on("r-leaflet@2.1.1:", type=("build", "run"))
	depends_on("r-plotly@4.9.3:", type=("build", "run"))
	depends_on("r-rdpack@2.1.1:", type=("build", "run"))
	depends_on("r-matrixstats@0.58:", type=("build", "run"))
	depends_on("r-terra@1.6.47:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
