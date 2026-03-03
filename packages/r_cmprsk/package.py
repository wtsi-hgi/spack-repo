# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmprsk(RPackage):
	"""Subdistribution Analysis of Competing Risks

	Estimation, testing and regression modeling of
 subdistribution functions in competing risks, as described in Gray
 (1988), A class of K-sample tests for comparing the cumulative
 incidence of a competing risk, Ann. Stat. 16:1141-1154
 <DOI:10.1214/aos/1176350951>, and Fine JP and
 Gray RJ (1999), A proportional hazards model for the subdistribution
 of a competing risk, JASA, 94:496-509, <DOI:10.1080/01621459.1999.10474144>.
	"""
	
	homepage = "https://www.R-project.org"
	cran = "cmprsk" 

	version("2.2-11", md5="080880c7b286a36d7df18dfe833b580a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
