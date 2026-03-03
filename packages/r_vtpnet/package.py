# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVtpnet(RPackage):
	"""variant-transcription factor-phenotype networks

	variant-transcription factor-phenotype networks, inspired by Maurano et al., Science (2012), PMID 22955828
	"""
	
	bioc = "vtpnet" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/vtpnet_0.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/vtpnet/vtpnet_0.42.0.tar.gz"]

	version("0.42.0", md5="a3a08b447e9ce26fafeed6fe2c515e10")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-gwascat", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
