# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeHsapiensNcbiT2tChm13v20(RPackage):
	"""T2T-CHM13v2.0 assembly (Homo sapiens) wrapped in a BSgenome object

	The T2T-CHM13v2.0 assembly (accession GCA_009914755.4), as submitted to NCBI by the T2T Consortium, and wrapped in a BSgenome object. Companion paper: "The complete sequence of a human genome" by Nurk S, Koren S, Rhie A, Rautiainen M, et al. Science, 2022.
	"""
	
	bioc = "BSgenome.Hsapiens.NCBI.T2T.CHM13v2.0" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Hsapiens.NCBI.T2T.CHM13v2.0_1.5.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Hsapiens.NCBI.T2T.CHM13v2.0/BSgenome.Hsapiens.NCBI.T2T.CHM13v2.0_1.5.0.tar.gz"]

	version("1.5.0", md5="22a99174e1e17718e0b4f8b66f32fd9b", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Hsapiens.NCBI.T2T.CHM13v2.0_1.5.0.tar.gz")
	version("1.5.0", md5="22a99174e1e17718e0b4f8b66f32fd9b", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Hsapiens.NCBI.T2T.CHM13v2.0_1.5.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))

