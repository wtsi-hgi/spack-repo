# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowsortedBlood450k(RPackage):
	"""Illumina HumanMethylation data on sorted blood cell populations

	Raw data objects for the Illumina 450k DNA methylation microarrays, and an object depicting which CpGs on the array are associated with cell type.
	"""
	
	bioc = "FlowSorted.Blood.450k" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/FlowSorted.Blood.450k_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/FlowSorted.Blood.450k/FlowSorted.Blood.450k_1.40.0.tar.gz"]

	version("1.40.0", md5="f88422c2d8a2f7ce4ca968292adfc8ab")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-minfi@1.21.2:", type=("build", "run"))

	# experiment