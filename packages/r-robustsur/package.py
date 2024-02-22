# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustsur(RPackage):
	"""Robust Estimation for Seemingly Unrelated Regression Models

	Data sets are often corrupted by outliers. When data are multivariate outliers can be classified as case-wise or cell-wise. The latters are particularly challenge to handle. We implement a robust estimation procedure for Seemingly Unrelated Regression Models which is able to cope well with both type of outliers. Giovanni Saraceno, Fatemah Alqallaf, Claudio Agostinelli (2021) <arXiv:2107.00975>. 
	"""
	
	cran = "robustsur" 

	version("0.0-7", md5="3625025f516280bbd3b678b0c47cc6e1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-robreg3s", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gse", type=("build", "run"))
