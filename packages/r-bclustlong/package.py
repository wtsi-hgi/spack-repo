# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBclustlong(RPackage):
	"""A Dirichlet Process Mixture Model for Clustering Longitudinal
Gene Expression Data

	Many clustering methods have been proposed, but
    most of them cannot work for longitudinal gene expression data. 
    'BClustLonG' is a package that allows us to perform clustering analysis for 
    longitudinal gene expression data. It adopts a linear-mixed effects framework 
    to model the trajectory of genes over time, while clustering is jointly 
    conducted based on the regression coefficients obtained from all genes. 
    To account for the correlations among genes and alleviate the 
    high dimensionality challenges, factor analysis models are adopted
    for the regression coefficients. The Dirichlet process prior distribution 
    is utilized for the means of the regression coefficients to induce clustering.
    This package allows users to specify which variables to use for clustering 
    (intercepts or slopes or both) and whether a factor analysis model is desired.
    More details about this method can be found in Jiehuan Sun, et al. (2017) <doi:10.1002/sim.7374>.
	"""
	
	cran = "BClustLonG" 

	version("0.1.3", md5="3a1706574e7487e3219746e22ede11de")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass@7.3.47:", type=("build", "run"))
	depends_on("r-lme4@1.1.13:", type=("build", "run"))
	depends_on("r-mcclust@1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
