# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKfpca(RPackage):
	"""Kendall Functional Principal Component Analysis

	Implementation for Kendall functional principal component analysis. Kendall functional principal component analysis is a robust functional principal component analysis technique for non-Gaussian functional/longitudinal data. The crucial function of this package is KFPCA() and KFPCA_reg(). Moreover, least square estimates of functional principal component scores are also provided. Refer to Rou Zhong, Shishi Liu, Haocheng Li, Jingxiao Zhang. (2021) <arXiv:2102.01286>. Rou Zhong, Shishi Liu, Haocheng Li, Jingxiao Zhang. (2021) <doi:10.1016/j.jmva.2021.104864>.
	"""
	
	cran = "KFPCA" 

	version("2.0", md5="dcb8c02c215f4b8cc896a25d1353436d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-kader", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-fdapace", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
