# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrwbmetareg(RPackage):
	"""Cluster Robust Wild Bootstrap Meta Regression

	In meta regression sometimes the studies have multiple effects that are correlated. For this reason cluster robust standard errors must be computed. However, since the clusters are unbalanced the wild bootstrap is suggested. See Oczkowski E. and Doucouliagos H. (2015). "Wine prices and quality ratings: a meta-regression analysis". American Journal of Agricultural Economics, 97(1): 103--121. <doi:10.1093/ajae/aau057> and Cameron A. C., Gelbach J. B. and Miller D. L. (2008). "Bootstrap-based improvements for inference with clustered errors". The Review of Economics and Statistics, 90(3): 414--427. <doi:10.1162/rest.90.3.414>.
	"""
	
	cran = "crwbmetareg" 

	version("1.0", md5="faf790b3c308ff45917d7761d5aa139d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-rfast2", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
