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
	urls = ["https://www.bioconductor.org/packages/3.18/workflows/src/contrib/CAGEWorkflow_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/workflows/src/contrib/Archive/CAGEWorkflow/CAGEWorkflow_1.18.0.tar.gz"]

	version("1.18.0", md5="0e15ef3a7d9b37b7945c17aaf45d07e0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cagefightr", type=("build", "run"))
	depends_on("r-nanotubes", type=("build", "run"))

	# workflow