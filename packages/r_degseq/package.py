# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDegseq(RPackage):
	"""Identify Differentially Expressed Genes from RNA-seq data

	DEGseq is an R package to identify differentially expressed genes from RNA-Seq data.
	"""
	
	bioc = "DEGseq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DEGseq_1.56.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DEGseq/DEGseq_1.56.1.tar.gz"]

	version("1.56.1", md5="cc89e25cb7e9afc38b5fb2bba34722b5")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
