# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIasva(RPackage):
	"""Iteratively Adjusted Surrogate Variable Analysis

	Iteratively Adjusted Surrogate Variable Analysis (IA-SVA) is a statistical framework to uncover hidden sources of variation even when these sources are correlated. IA-SVA provides a flexible methodology to i) identify a hidden factor for unwanted heterogeneity while adjusting for all known factors; ii) test the significance of the putative hidden factor for explaining the unmodeled variation in the data; and iii), if significant, use the estimated factor as an additional known factor in the next iteration to uncover further hidden factors.
	"""
	
	bioc = "iasva" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iasva_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iasva/iasva_1.20.0.tar.gz"]

	version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="625e5395f786afbea9a8784e591a9b7e991096e7f1039d15a6d6849d1f1ebfe0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
