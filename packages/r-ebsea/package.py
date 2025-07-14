# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbsea(RPackage):
	"""Exon Based Strategy for Expression Analysis of genes

	Calculates differential expression of genes based on exon counts of genes obtained from RNA-seq sequencing data.
	"""
	
	bioc = "EBSEA" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/EBSEA_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/EBSEA/EBSEA_1.30.0.tar.gz"]

    version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="a373d8d37c857a9058d250398fc9dede7b0f7c4add523ba0807ba3def1675af9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-empiricalbrownsmethod", type=("build", "run"))
