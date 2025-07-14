# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowertcr(RPackage):
	"""Model-Based Comparative Analysis of the TCR Repertoire

	This package provides a model for the clone size distribution of the TCR repertoire. Further, it permits comparative analysis of TCR repertoire libraries based on theoretical model fits.
	"""
	
	bioc = "powerTCR"

	version("1.28.0", commit="9e40023a48c11fb5e2d94314ad9bf1daef71a40a")
	version("1.22.0", commit="78a217ebb807b10b08b214da429e2f5c3edd980f")

	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-evmix", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-truncdist", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
