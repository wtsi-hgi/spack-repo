# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrfa(RPackage):
	"""Group Factor Analysis

	Several group factor analysis algorithms are implemented, including Canonical Correlation-based Estimation by Choi et al. (2021) <doi:10.1016/j.jeconom.2021.09.008> , Generalised Canonical Correlation Estimation by Lin and Shin (2022) <doi:10.2139/ssrn.4295429>, Circularly Projected Estimation by Chen (2022) <doi:10.1080/07350015.2022.2051520>, and the approach we recently proposed, named Aggregated Projection Method. 
	"""
	
	cran = "GrFA" 

	version("0.1.1", md5="cf86fcec7461dc57abf418124ebe68c4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
