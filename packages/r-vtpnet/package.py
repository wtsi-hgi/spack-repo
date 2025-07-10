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

	version("0.42.0", sha256="4f2520efa3c0bb0cc9272d63d3a20d72b8bbe50cf1dcc34d588ab1353edea014")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-gwascat", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
