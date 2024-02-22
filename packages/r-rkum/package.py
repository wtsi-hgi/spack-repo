# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRkum(RPackage):
	"""Robust Kernel Unsupervised Methods

	Robust  kernel center matrix, robust  kernel cross-covariance operator for kernel unsupervised methods, kernel canonical correlation analysis, 
 influence function of identifying significant outliers or atypical objects from multimodal datasets. Alam, M. A,  Fukumizu, K., Wang  Y.-P. (2018) <doi:10.1016/j.neucom.2018.04.008>.
   Alam, M. A,  Calhoun, C. D.,  Wang  Y.-P. (2018) <doi:10.1016/j.csda.2018.03.013>.
	"""
	
	cran = "RKUM" 

	version("0.1.1.1", md5="2a9e7e95500579e3a870d54e8419a950")

