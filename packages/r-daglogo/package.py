# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaglogo(RPackage):
	"""dagLogo: a Bioconductor package for visualizing conserved amino acid sequence pattern in groups based on probability theory

	Visualize significant conserved amino acid sequence pattern in groups based on probability theory.
	"""
	
	bioc = "dagLogo" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/dagLogo_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/dagLogo/dagLogo_1.40.0.tar.gz"]

	version("1.40.0", sha256="63161742ae285beff886b064a4dacbd8086c708549b44a52d4d173fbb59b38dd")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-uniprot-ws", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-motifstack", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
