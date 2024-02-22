# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStlnpp(RPackage):
	"""Spatio-Temporal Analysis of Point Patterns on Linear Networks

	Statistical analysis of spatio-temporal point processes on linear networks. This packages provides tools to visualise and analyse spatio-temporal point patterns on linear networks using first- and second-order summary statistics.
	"""
	
	cran = "stlnpp" 

	version("0.3.10", md5="45d7e664b20eec54ba783c09da1227df")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-spatstat@2.0.0:", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-linnet", type=("build", "run"))
