# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCageworkflow(RPackage):
	"""A step-by-step guide to analyzing CAGE data using R/Bioconductor

	Workflow for analyzing Cap Analysis of Gene Expression (CAGE) data using R/Bioconductor.
	"""
	
	bioc = "CAGEWorkflow"

	version("1.24.0", commit="0819ec30e380d5dcaabca667aed87a2a4b634fed")
	version("1.18.0", commit="e4cca1f6532706dcc353aee3aa1bc3671cdda765")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cagefightr", type=("build", "run"))
	depends_on("r-nanotubes", type=("build", "run"))

