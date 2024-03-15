# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowsortedCordblood450k(RPackage):
	"""Illumina 450k data on sorted cord blood cells

	Raw data objects to be used for cord blood cell proportion estimation in minfi.
	"""
	
	bioc = "FlowSorted.CordBlood.450k" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/FlowSorted.CordBlood.450k_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/FlowSorted.CordBlood.450k/FlowSorted.CordBlood.450k_1.30.0.tar.gz"]

	version("1.30.0", md5="fca81b7412af68100d7aed4d57d5fc59")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-minfi@1.21.2:", type=("build", "run"))

	# experiment