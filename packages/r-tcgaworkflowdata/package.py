# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcgaworkflowdata(RPackage):
	"""Data for TCGA Workflow

	This experimental data package contains 11 data sets necessary to follow the "TCGA Workflow: Analyze cancer genomics and epigenomics data using Bioconductor packages".
	"""
	
	homepage = "https://f1000research.com/articles/5-1542/v2"
	bioc = "TCGAWorkflowData"

	version("1.32.0", commit="9a3836c2fe3a5bad929377b09e4809c5bca792ad")
	version("1.26.0", commit="556a0521414e7244b1f2e93b360904050b42d54b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

