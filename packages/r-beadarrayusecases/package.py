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

	version("1.46.0", commit="7003003d3d39a5c197b0f3744a76039457339552")
	version("1.40.0", commit="85aa053bb307c1722d13d3a1a90b6d4df20042b0")

	depends_on("r-beadarray@2.3.18:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))

