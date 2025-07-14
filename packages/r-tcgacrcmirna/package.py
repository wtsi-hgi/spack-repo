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

    version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="5550127c27200fc2b2209b7c6fb19792cde3c4f2dc5e7f1d6fbca1b2aa902c63")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

