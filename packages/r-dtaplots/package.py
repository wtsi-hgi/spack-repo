# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtaplots(RPackage):
	"""Creates Plots Accompanying Bayesian Diagnostic Test Accuracy
Meta-Analyses

	Function to create forest plots. Functions to use posterior samples from Bayesian bivariate meta-analysis model, Bayesian hierarchical summary receiver operating characteristic (HSROC) meta-analysis model or Bayesian latent class (LC) meta-analysis model to create Summary Receiver Operating Characteristic (SROC) plots using methods described by Harbord et al (2007)<doi:10.1093/biostatistics/kxl004>.
	"""
	
	cran = "DTAplots" 

	version("1.0.2.5", md5="db1c0ab3aa83a6c0f7566f298d10c44d")

	depends_on("r@3.5:", type=("build", "run"))
