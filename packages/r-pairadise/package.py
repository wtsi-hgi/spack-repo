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

    version("1.24.1", tag="RELEASE_3_21")
	version("1.18.0", sha256="f95eec0a7a3743142fdc4f39bec8c59aca6644a09a3e9cd755f4c4ad776727fc")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
