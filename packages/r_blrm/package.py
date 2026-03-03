# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlrm(RPackage):
	"""Dose Escalation Design in Phase I Oncology Trial Using Bayesian
Logistic Regression Modeling

	Design dose escalation using Bayesian logistic regression modeling in Phase I oncology trial.
	"""
	
	cran = "blrm" 

	version("1.0-2", md5="9d91de8aef8501188a19c7595602812c")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
