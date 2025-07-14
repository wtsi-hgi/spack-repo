# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImman(RPackage):
	"""Interlog protein network reconstruction by Mapping and Mining ANalysis

	Reconstructing Interlog Protein Network (IPN) integrated from several Protein protein Interaction Networks (PPINs). Using this package, overlaying different PPINs to mine conserved common networks between diverse species will be applicable.
	"""
	
	bioc = "IMMAN" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/IMMAN_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/IMMAN/IMMAN_1.22.0.tar.gz"]

    version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="5a5369e6c2d1a6a07017db76993dd625bd2568c6112388af1dd535bd19245b73")

	depends_on("r-stringdb", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
