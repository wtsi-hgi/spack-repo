# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROtrkm(RPackage):
	"""Optimal Treatment Regimes in Survival Contexts with
Kaplan-Meier-Like Estimators

	Provide methods for estimating optimal treatment regimes in survival contexts 
    with Kaplan-Meier-like estimators when no unmeasured confounding assumption is 
    satisfied (Jiang, R., Lu, W., Song, R., and Davidian, M. (2017) <doi:10.1111/rssb.12201>) 
    and when no unmeasured confounding assumption fails to hold and a binary instrument 
    is available (Xia, J., Zhan, Z., Zhang, J. (2022) <arXiv:2210.05538>).
	"""
	
	cran = "otrKM" 

	version("0.2.1", md5="6f82f65d781f2c2a234c3638c677d27c")

	depends_on("r@3.10:", type=("build", "run"))
	depends_on("r-rgenoud", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
