# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeadarrayusecases(RPackage):
	"""Analysing Illumina BeadArray expression data using Bioconductor

	Example data files and use cases for processing Illumina BeadArray expression data using Bioconductor
	"""
	
	bioc = "BeadArrayUseCases" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/BeadArrayUseCases_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/BeadArrayUseCases/BeadArrayUseCases_1.40.0.tar.gz"]

	version("1.40.0", sha256="3ed2083d2761d9a59f24ab4bfe2bdb24500e77d92e6c2e5f22f6632ead465914")

	depends_on("r-beadarray@2.3.18:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))

