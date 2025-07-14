# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomicinteractionnodes(RPackage):
	"""A R/Bioconductor package to detect the interaction nodes from HiC/HiChIP/HiCAR data

	The GenomicInteractionNodes package can import interactions from bedpe file and define the interaction nodes, the genomic interaction sites with multiple interaction loops. The interaction nodes is a binding platform regulates one or multiple genes. The detected interaction nodes will be annotated for downstream validation.
	"""
	
	homepage = "https://github.com/jianhong/GenomicInteractionNodes"
	bioc = "GenomicInteractionNodes" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GenomicInteractionNodes_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GenomicInteractionNodes/GenomicInteractionNodes_1.6.0.tar.gz"]

	version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="4c06511ba207d07b071317972fcfb9bc0c45d5d7958b8b1be9c03113a7ecc004")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
