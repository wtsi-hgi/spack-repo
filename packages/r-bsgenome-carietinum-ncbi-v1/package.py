# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeCarietinumNcbiV1(RPackage):
	"""Cicer arietinum (Chickpea) full genome (NCBI version ASM33114v1)

	Full genome sequences for Cicer arietinum (Chickpea) as provided by NCBI (ASM33114v1, Jan. 2013) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Carietinum.NCBI.v1" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Carietinum.NCBI.v1_1.0.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Carietinum.NCBI.v1/BSgenome.Carietinum.NCBI.v1_1.0.0.tar.gz"]

	version("1.0.0", md5="eef018ecce6d32852aa18ac39cf377c6", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Carietinum.NCBI.v1_1.0.0.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation