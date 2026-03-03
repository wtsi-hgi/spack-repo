# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwangrdc(RPackage):
	"""Gradient Boosting for Linkage Failure in FSRDCs

	Provides functions for gradient boosted weighting to correct linkage 
    failures or generate comparison groups.
	"""
	
	cran = "twangRDC" 

	version("1.0", md5="d9e1ce8dc36219c0a9de4769f4a928d8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrixmodels", type=("build", "run"))
