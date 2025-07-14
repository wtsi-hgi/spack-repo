# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynapter(RPackage):
	"""Label-free data analysis pipeline for optimal identification and quantitation

	The synapter package provides functionality to reanalyse label-free proteomics data acquired on a Synapt G2 mass spectrometer. One or several runs, possibly processed with additional ion mobility separation to increase identification accuracy can be combined to other quantitation files to maximise identification and quantitation accuracy.
	"""
	
	homepage = "https://lgatto.github.io/synapter/"
	bioc = "synapter" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/synapter_2.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/synapter/synapter_2.26.0.tar.gz"]

    version("2.32.0", tag="RELEASE_3_21")
	version("2.26.0", sha256="03cd1fb5c89df4c1bcb5f6937086fa07a76d04a89023854bf42344ab95379f31")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-msnbase@2.1.2:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-cleaver@1.3.3:", type=("build", "run"))
	depends_on("r-readr@0.2:", type=("build", "run"))
	depends_on("r-rmarkdown@1:", type=("build", "run"))
