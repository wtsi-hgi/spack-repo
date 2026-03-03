# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialwarnings(RPackage):
	"""Spatial Early Warning Signals of Ecosystem Degradation

	Tools to compute and assess significance of early-warnings signals (EWS) of ecosystem degradation on raster data sets. EWS are metrics derived from the observed spatial structure of an ecosystem -- e.g. spatial autocorrelation -- that increase before an ecosystem undergoes a non-linear transition (Genin et al. (2018) <doi:10.1111/2041-210X.13058>).
	"""
	
	homepage = "https://github.com/spatial-ews/spatialwarnings"
	cran = "spatialwarnings" 

	version("3.0.3", md5="97e505c2b3fb8136241875708af8a65f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-segmented", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
