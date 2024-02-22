# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIadapt(RPackage):
	"""Two-Stage Adaptive Dose-Finding Clinical Trial Design

	Simulate and implement early phase two-stage adaptive dose-finding design for binary and quasi-continuous toxicity endpoints. See Chiuzan et al. (2018) for further reading <DOI:10.1080/19466315.2018.1462727>.
	"""
	
	cran = "iAdapt" 

	version("2.0.1", md5="cdab8d108671981ec7a5b1173412803a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
