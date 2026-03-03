# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovregrf(RPackage):
	"""Covariance Regression with Random Forests

	Covariance Regression with Random Forests (CovRegRF) is a
    random forest method for estimating the covariance matrix of a
    multivariate response given a set of covariates. Random forest trees
    are built with a new splitting rule which is designed to maximize the
    distance between the sample covariance matrix estimates of the child
    nodes. The method is described in Alakus et al. (2023)
    <doi:10.1186/s12859-023-05377-y>. 'CovRegRF' uses 'randomForestSRC' package
    (Ishwaran and Kogalur, 2022) 
    <https://cran.r-project.org/package=randomForestSRC> by freezing at the
    version 3.1.0. The custom splitting rule feature is utilised to apply the
    proposed splitting rule. The 'randomForestSRC' package implements 'OpenMP' 
    by default, contingent upon the support provided by the target architecture 
    and operating system. In this package, 'LAPACK' and 'BLAS' libraries are 
    used for matrix decompositions.
	"""
	
	cran = "CovRegRF" 

	version("2.0.0", md5="cc8dfe2a6ea9b211e22d851128672704")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
