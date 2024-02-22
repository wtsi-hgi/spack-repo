# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimffpe(RPackage):
	"""NGS Read Simulator for FFPE Tissue

	The NGS (Next-Generation Sequencing) reads from FFPE (Formalin-Fixed Paraffin-Embedded) samples contain numerous artifact chimeric reads (ACRS), which can lead to false positive structural variant calls. These ACRs are derived from the combination of two single-stranded DNA (ss-DNA) fragments with short reverse complementary regions (SRCRs). This package simulates these artifact chimeric reads as well as normal reads for FFPE samples on the whole genome / several chromosomes / large regions.
	"""
	
	bioc = "SimFFPE" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SimFFPE_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SimFFPE/SimFFPE_1.14.0.tar.gz"]

	version("1.14.0", md5="95d6710ea184127f659f0c6f7786234c")

	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
