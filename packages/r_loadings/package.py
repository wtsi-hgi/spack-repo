# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLoadings(RPackage):
	"""Loadings for Principal Component Analysis and Partial Least
Squares

	Computing statistical hypothesis testing for loading in principal component analysis (PCA) (Yamamoto, H. et al. (2014) <doi:10.1186/1471-2105-15-51>), orthogonal smoothed PCA (OS-PCA) (Yamamoto, H. et al. (2021) <doi:10.3390/metabo11030149>), one-sided kernel PCA (Yamamoto, H. (2023) <doi:10.51094/jxiv.262>), partial least squares (PLS) and PLS discriminant analysis (PLS-DA) (Yamamoto, H. et al. (2009) <doi:10.1016/j.chemolab.2009.05.006>), PLS with rank order of groups (PLS-ROG) (Yamamoto, H. (2017) <doi:10.1002/cem.2883>), regularized canonical correlation analysis discriminant analysis (RCCA-DA) (Yamamoto, H. et al. (2008) <doi:10.1016/j.bej.2007.12.009>), multiset PLS and PLS-ROG (Yamamoto, H. (2022) <doi:10.1101/2022.08.30.505949>).
	"""
	
	cran = "loadings" 

	version("0.4.1", md5="0774425a72e0b276e719786efe81c191")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-geigen", type=("build", "run"))
