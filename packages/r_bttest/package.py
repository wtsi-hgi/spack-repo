# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBttest(RPackage):
	"""Estimate the Number of Factors in Large Nonstationary Datasets

	
  Large panel data sets are often subject to common trends. However, it can be difficult to determine the exact number of these common factors and analyse their properties.
  The package implements the Barigozzi and Trapani (2022) <doi:10.1080/07350015.2021.1901719> test, which not only provides an efficient way of estimating the number of common factors in large nonstationary panel data sets, but also gives further insights on factor classes. The routine identifies the existence of (i) a factor subject to a linear trend, (ii) the number of zero-mean I(1) and (iii) zero-mean I(0) factors.
  Furthermore, the package includes the Integrated Panel Criteria by Bai (2004) <doi:10.1016/j.jeconom.2003.10.022> that provide a complementary measure for the number of factors.
	"""
	
	homepage = "https://github.com/Paul-Haimerl/BTtest"
	cran = "BTtest" 

	version("0.10.1", md5="ac2124ee164525d91e49b6a240edebc4")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
