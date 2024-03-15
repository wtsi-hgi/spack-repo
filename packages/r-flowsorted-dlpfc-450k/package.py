# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowsortedDlpfc450k(RPackage):
	"""Illumina HumanMethylation data on sorted frontal cortex cell populations

	Raw data objects for the Illumina 450k DNA methylation microarrays.
	"""
	
	bioc = "FlowSorted.DLPFC.450k" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/FlowSorted.DLPFC.450k_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/FlowSorted.DLPFC.450k/FlowSorted.DLPFC.450k_1.38.0.tar.gz"]

	version("1.38.0", md5="ad95a51f7e8bcf7c0bec6dda80eb0a92")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-minfi@1.21.2:", type=("build", "run"))

	# experiment