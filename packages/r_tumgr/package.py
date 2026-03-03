# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTumgr(RPackage):
	"""Tumor Growth Rate Analysis

	A tool to obtain tumor growth rates from clinical trial patient data.  Output includes individual and summary data for tumor growth rate estimates as well as optional plots of the observed and predicted tumor quantity over time.
	"""
	
	homepage = "https://wilkersj.shinyapps.io/tumgrShiny"
	cran = "tumgr" 

	version("0.0.4", md5="ae4099ac1fb166364deb662fa1887f51")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
