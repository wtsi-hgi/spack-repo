# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLagsarlmtree(RPackage):
	"""Spatial Lag Model Trees

	Model-based linear model trees adjusting for spatial correlation using a
             simultaneous autoregressive spatial lag, Wagner and Zeileis (2019)
	     <doi:10.1111/geer.12146>.
	"""
	
	cran = "lagsarlmtree" 

	version("1.0-1", md5="1c31f2d262335ff3bfd64c1e04ca719b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-spatialreg", type=("build", "run"))
	depends_on("r-formula@1.2.1:", type=("build", "run"))
