# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSilggm(RPackage):
	"""Statistical Inference of Large-Scale Gaussian Graphical Model in
Gene Networks

	Provides a general framework to perform statistical inference of each gene pair 
        and global inference of whole-scale gene pairs in gene networks using the well known 
        Gaussian graphical model (GGM) in a time-efficient manner. We focus on the high-dimensional 
        settings where p (the number of genes) is allowed to be far larger than n (the number of subjects). 
        Four main approaches are supported in this package: (1) the bivariate nodewise scaled Lasso 
        (Ren et al (2015) <doi:10.1214/14-AOS1286>) (2) the de-sparsified nodewise scaled Lasso 
        (Jankova and van de Geer (2017) <doi:10.1007/s11749-016-0503-5>) (3) the de-sparsified 
        graphical Lasso (Jankova and van de Geer (2015) <doi:10.1214/15-EJS1031>) (4) the GGM 
        estimation with false discovery rate control (FDR) using scaled Lasso or Lasso 
        (Liu (2013) <doi:10.1214/13-AOS1169>). Windows users should install 'Rtools' before the 
        installation of this package.
	"""
	
	cran = "SILGGM" 

	version("1.0.0", md5="6c126b11fc1d640771164babe101da8a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
