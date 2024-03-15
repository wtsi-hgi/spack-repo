# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcgacrcmirna(RPackage):
	"""TCGA CRC 450 miRNA dataset

	colorectal cancer miRNA profile provided by TCGA
	"""
	
	bioc = "TCGAcrcmiRNA" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/TCGAcrcmiRNA_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/TCGAcrcmiRNA/TCGAcrcmiRNA_1.22.0.tar.gz"]

	version("1.22.0", md5="451d09b5ec341d7e92211a1d42c35947")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

	# experiment