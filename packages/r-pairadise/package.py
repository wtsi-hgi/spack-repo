# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPairadise(RPackage):
	"""PAIRADISE: Paired analysis of differential isoform expression

	This package implements the PAIRADISE procedure for detecting differential isoform expression between matched replicates in paired RNA-Seq data.
	"""
	
	bioc = "PAIRADISE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PAIRADISE_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PAIRADISE/PAIRADISE_1.18.0.tar.gz"]

	version("1.18.0", md5="2a3889d2380363b7a9b0ee3c75ef0891")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
