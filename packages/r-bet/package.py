# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBet(RPackage):
	"""Binary Expansion Testing

	Nonparametric detection of nonuniformity and dependence with Binary Expansion Testing (BET). See Kai Zhang (2019) BET on Independence, Journal of the American Statistical Association, 114:528, 1620-1637, <DOI:10.1080/01621459.2018.1537921>, Kai Zhang, Zhigen Zhai, and Wen Zhou. (2021). BEAUTY Powered BEAST, <arXiv:2103.00674>  and Wan Zhang, Zhigen Zhao, Michael Baiocchi, Yao Li, Kai Zhang. SorBET: A Fast and Powerful Algorithm to Test Dependence of Variables, Techinical report, 2023.
	"""
	
	cran = "BET" 

	version("0.5.3", md5="e3174edd19ebc8c3ad727cd2d615edf6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
