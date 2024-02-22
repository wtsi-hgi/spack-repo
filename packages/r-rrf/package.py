# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrf(RPackage):
	"""Regularized Random Forest

	Feature Selection with Regularized Random Forest. This
    package is based on the 'randomForest' package by Andy Liaw.
    The key difference is the RRF() function that builds a
    regularized random forest. Fortran original by Leo Breiman 
    and Adele Cutler, R port by Andy Liaw and Matthew Wiener, 
    Regularized random forest for classification by Houtao Deng, 
    Regularized random forest for regression by Xin Guan.
    Reference: Houtao Deng (2013) <arXiv:1306.0237>.
	"""
	
	homepage = "https://sites.google.com/site/houtaodeng/rrf"
	cran = "RRF" 

	version("1.9.4", md5="77af4eacdd28eae5f73267a29ad04797")

	depends_on("r@2.5:", type=("build", "run"))
