# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCombo(RPackage):
	"""Correcting Misclassified Binary Outcomes in Association Studies

	Use frequentist and Bayesian methods to estimate parameters from a
  binary outcome misclassification model. These methods correct for the problem
  of "label switching" by assuming that correct outcome classification occurs
  in at least 50% of observations. A description of the analysis methods is
  available in Hochstedler and Wells (2023) <arXiv:2303.10215>. 
	"""
	
	cran = "COMBO" 

	version("1.0.0", md5="8c2ad25606f08db214ff6f7325e958f8")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-tidyr@1.2.1:", type=("build", "run"))
	depends_on("r-matrix@1.4.1:", type=("build", "run"))
	depends_on("r-rjags@4.13:", type=("build", "run"))
	depends_on("r-turboem@2021.1:", type=("build", "run"))
	depends_on("r-samba@0.9:", type=("build", "run"))
