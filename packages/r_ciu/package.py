# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCiu(RPackage):
	"""Contextual Importance and Utility

	Implementation of the Contextual Importance and Utility 
    (CIU) concepts for Explainable AI (XAI). A recent description of CIU
    can be found in e.g. Främling (2020) <arXiv:2009.13996>.
	"""
	
	cran = "ciu" 

	version("0.6.0", md5="e4c353fdd5322607b5028090f86ce0ed")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
