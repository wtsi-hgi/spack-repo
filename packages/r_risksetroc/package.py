# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRisksetroc(RPackage):
	"""Riskset ROC Curve Estimation from Censored Survival Data

	Compute time-dependent Incident/dynamic accuracy measures
        (ROC curve, AUC, integrated AUC )from censored survival data
        under proportional or non-proportional hazard assumption of
        Heagerty & Zheng (Biometrics, Vol 61 No 1, 2005, PP 92-105).
	"""
	
	cran = "risksetROC" 

	version("1.0.4.1", md5="cebe6c8bcfbbe928bad409ea908049e1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
