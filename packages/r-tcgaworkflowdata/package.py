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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/TCGAWorkflowData_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/TCGAWorkflowData/TCGAWorkflowData_1.26.0.tar.gz"]

	version("1.26.0", md5="cbba498f1922aeedadf96a1911a81751")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

	# experiment