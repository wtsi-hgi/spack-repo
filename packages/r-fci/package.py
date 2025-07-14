# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFci(RPackage):
	"""f-divergence Cutoff Index for Differential Expression Analysis in Transcriptomics and Proteomics

	(f-divergence Cutoff Index), is to find DEGs in the transcriptomic & proteomic data, and identify DEGs by computing the difference between the distribution of fold-changes for the control-control and remaining (non-differential) case-control gene expression ratio data. fCI provides several advantages compared to existing methods.
	"""
	
	bioc = "fCI" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/fCI_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/fCI/fCI_1.32.0.tar.gz"]

    version("1.38.0", tag="RELEASE_3_21")
	version("1.32.0", sha256="1fbe66b4235e58c212fa378cb1029225f7caeebf3e87cc078bc5174946ec27b0")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
