# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowsortedCordbloodnorway450k(RPackage):
	"""Illumina HumanMethylation data on sorted cord blood cell populations

	Raw data objects for the Illumina 450k DNA methylation microarrays, for cell type composition estimation.
	"""
	
	homepage = "https://bitbucket.com/kasperdanielhansen/Illumina_CordBlood"
	bioc = "FlowSorted.CordBloodNorway.450k" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/FlowSorted.CordBloodNorway.450k_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/FlowSorted.CordBloodNorway.450k/FlowSorted.CordBloodNorway.450k_1.28.0.tar.gz"]

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="22661f01c4f2990f619ecee211818017712e23cf1eac57bca311c2aea682199a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-minfi@1.21.2:", type=("build", "run"))

