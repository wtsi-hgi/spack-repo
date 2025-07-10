# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLumibarnes(RPackage):
	"""Barnes Benchmark Illumina Tissues Titration Data

	The Barnes benchmark dataset can be used to evaluate the algorithms for Illumina microarrays. It measured a titration series of two human tissues, blood and placenta, and includes six samples with the titration ratio of blood and placenta as 100:0, 95:5, 75:25, 50:50, 25:75 and 0:100. The samples were hybridized on HumanRef-8 BeadChip (Illumina, Inc) in duplicate. The data is loaded as an LumiBatch Object (see documents in the lumi package).
	"""
	
	bioc = "lumiBarnes" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/lumiBarnes_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/lumiBarnes/lumiBarnes_1.42.0.tar.gz"]

	version("1.42.0", sha256="c2dff605ff67e5f08cf53c8cfc3aed0755c6abd2b799275a75cfd729d5d147b0")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-lumi@1.1:", type=("build", "run"))

