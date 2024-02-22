# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdpclust(RPackage):
	"""Fast Clustering Using Adaptive Density Peak Detection

	An implementation of ADPclust clustering procedures (Fast
    Clustering Using Adaptive Density Peak Detection). The work is built and
    improved upon the idea of Rodriguez and Laio (2014)<DOI:10.1126/science.1242072>. 
    ADPclust clusters data by finding density peaks in a density-distance plot 
    generated from local multivariate Gaussian density estimation. It includes 
    an automatic centroids selection and parameter optimization algorithm, which 
    finds the number of clusters and cluster centroids by comparing average 
    silhouettes on a grid of testing clustering results; It also includes a user 
    interactive algorithm that allows the user to manually selects cluster 
    centroids from a two dimensional "density-distance plot". Here is the 
    research article associated with this package: "Wang, Xiao-Feng, and 
    Yifan Xu (2015)<DOI:10.1177/0962280215609948> Fast clustering using adaptive 
    density peak detection." Statistical methods in medical research". url:
    http://smm.sagepub.com/content/early/2015/10/15/0962280215609948.abstract. 
	"""
	
	homepage = "https://github.com/ethanyxu/ADPclust"
	cran = "ADPclust" 

	version("0.7", md5="c86d81fd7b348df8d54ab07f16a29597")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
