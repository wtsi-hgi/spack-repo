# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrornaome(RPackage):
	"""SummarizedExperiment for the microRNAome project

	This package provides a SummarizedExperiment object of read counts for microRNAs across tissues, cell-types, and cancer cell-lines. The read count matrix was prepared and provided by the author of the study: Towards the human cellular microRNAome.
	"""
	
	bioc = "microRNAome" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/microRNAome_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/microRNAome/microRNAome_1.24.0.tar.gz"]

	version("1.24.0", md5="12d3baf395e82975bbcacfb9ff61a715")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

	# experiment