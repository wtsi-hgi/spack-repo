# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROutliertree(RPackage):
	"""Explainable Outlier Detection Through Decision Tree Conditioning

	Outlier detection method that flags suspicious values within observations,
  constrasting them against the normal values in a user-readable format, potentially
  describing conditions within the data that make a given outlier more rare.
  Full procedure is described in Cortes (2020) <arXiv:2001.00636>.
  Loosely based on the 'GritBot' <https://www.rulequest.com/gritbot-info.html> software.
	"""
	
	homepage = "https://github.com/david-cortes/outliertree"
	cran = "outliertree" 

	version("1.9.0", md5="43ff9a62c0d22520826e00dec5e83192")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcereal", type=("build", "run"))
