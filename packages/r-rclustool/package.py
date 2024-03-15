# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRclustool(RPackage):
	"""Graphical Toolbox for Clustering and Classification of Data
Frames

	Graphical toolbox for clustering and classification of data frames.
    It proposes a graphical interface to process clustering and classification methods on features
    data-frames, and to view initial data as well as resulted cluster or classes. According to the
    level of available labels, different approaches are proposed: unsupervised clustering,
    semi-supervised clustering and supervised classification. 
    To assess the processed clusters or classes, the toolbox can import and show some supplementary
    data formats: either profile/time series, or images. 
    These added information can help the expert to label clusters (clustering), or to constrain data
    frame rows (semi-supervised clustering), using Constrained spectral embedding algorithm by 
    Wacquet et al. (2013) <doi:10.1016/j.patrec.2013.02.003> and the methodology provided by 
    Wacquet et al. (2013) <doi:10.1007/978-3-642-35638-4_21>.
	"""
	
	homepage = "mawenzi.univ-littoral.fr/RclusTool"
	cran = "RclusTool" 

	version("0.91.6", md5="15876656847bce748dc5d7d8d043d593")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-tcltk2", type=("build", "run"))
	depends_on("r-tkrplot", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-conclust", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mda", type=("build", "run"))
	depends_on("r-mmand", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-searchtrees", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
