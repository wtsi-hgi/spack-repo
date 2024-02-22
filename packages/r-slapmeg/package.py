# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlapmeg(RPackage):
	"""Pathway Testing for Longitudinal Omics

	A self-contained hypothesis is tested for a given pathway of longitudinal omics. 'SlaPMEG' is a two-step procedure. First, a shared latent process mixed model is fitted over the longitudinal measures of omics in a pathway. This shared model allows deviation from the shared process at subject level (a random intercept, slope, or both per subject) and also at omic level (a random effect per omic). These random effects summarize the longitudinal trend of the observations which can be used to test for group differences using 'Globaltest' in the second step. If the pathway is large or the shared effect is small, the package fits a series of pairwise models and estimates the shared random effects based on them.
	"""
	
	cran = "SlaPMEG" 

	version("1.0.1", md5="f26029a19f6a0f8c95167e143a4038b7")

	depends_on("r-lme4@1.1.21:", type=("build", "run"))
	depends_on("r-lcmm@1.8.1:", type=("build", "run"))
	depends_on("r-globaltest@5.36:", type=("build", "run"))
	depends_on("r-magic@1.5.9:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
