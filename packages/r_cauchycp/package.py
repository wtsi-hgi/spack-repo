# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCauchycp(RPackage):
	"""Powerful Test for Survival Data under Non-Proportional Hazards

	An omnibus test of change-point Cox regression models to improve the statistical power of detecting signals of non-proportional hazards patterns. The technical details can be found in Hong Zhang, Qing Li, Devan Mehrotra and Judong Shen (2021) <arXiv:2101.00059>. Extensive simulation studies demonstrate that, compared to existing tests under non-proportional hazards, the proposed CauchyCP test 1) controls the type I error better at small alpha levels; 2) increases the power of detecting time-varying effects; and 3) is more computationally efficient.
	"""
	
	cran = "CauchyCP" 

	version("0.1.1", md5="af21ed79d00d761bf7fd076cc13922cc")

	depends_on("r-survival", type=("build", "run"))
