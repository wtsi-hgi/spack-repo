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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/powerTCR_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/powerTCR/powerTCR_1.22.0.tar.gz"]

	version("1.22.0", md5="6033da999bfcba4c2e80a45e358c3855")

	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-evmix", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-truncdist", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
