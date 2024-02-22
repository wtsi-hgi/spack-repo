# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFsn(RPackage):
	"""Rosenthal's Fail Safe Number and Related Functions

	Estimation of Rosenthal's fail safe number including confidence intervals. The relevant papers are the following. Konstantinos C. Fragkos, Michail Tsagris and Christos C. Frangos (2014). "Publication Bias in Meta-Analysis: Confidence Intervals for Rosenthal's Fail-Safe Number". International Scholarly Research Notices, Volume 2014. <doi:10.1155/2014/825383>. Konstantinos C. Fragkos, Michail Tsagris and Christos C. Frangos (2017). "Exploring the distribution for the estimator of Rosenthal's fail-safe number of unpublished studies in meta-analysis". Communications in Statistics-Theory and Methods, 46(11):5672--5684. <doi:10.1080/03610926.2015.1109664>.
	"""
	
	cran = "fsn" 

	version("0.2", md5="cb9bbea788d4c6e70e0c42fc0fe1934f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
