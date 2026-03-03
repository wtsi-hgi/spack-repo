# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKde1d(RPackage):
	"""Univariate Kernel Density Estimation

	Provides an efficient implementation of univariate local polynomial
    kernel density estimators that can handle bounded and discrete data. See 
    Geenens (2014) <arXiv:1303.4121>, 
    Geenens and Wang (2018) <arXiv:1602.04862>, 
    Nagler (2018a) <arXiv:1704.07457>, 
    Nagler (2018b) <arXiv:1705.05431>.
	"""
	
	homepage = "https://github.com/tnagler/kde1d"
	cran = "kde1d" 

	version("1.0.7", md5="e8b33f9c810c0c2c66ce1a2be853e302")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
