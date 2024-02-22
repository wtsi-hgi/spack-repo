# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtwclust(RPackage):
	"""Time Series Clustering Along with Optimizations for the Dynamic
Time Warping Distance

	Time series clustering along with optimized techniques related
    to the Dynamic Time Warping distance and its corresponding lower bounds.
    Implementations of partitional, hierarchical, fuzzy, k-Shape and TADPole
    clustering are available. Functionality can be easily extended with
    custom distance measures and centroid definitions. Implementations of
    DTW barycenter averaging, a distance based on global alignment kernels,
    and the soft-DTW distance and centroid routines are also provided. 
    All included distance functions have custom loops optimized for the 
    calculation of cross-distance matrices, including parallelization support.
    Several cluster validity indices are included.
	"""
	
	homepage = "https://github.com/asardaes/dtwclust"
	cran = "dtwclust" 

	version("5.5.12", md5="f0662dbcd10e57bfd91f3b1f245979ae")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-proxy@0.4.16:", type=("build", "run"))
	depends_on("r-dtw", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-flexclust", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppthread", type=("build", "run"))
