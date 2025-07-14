# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZfpkm(RPackage):
	"""A suite of functions to facilitate zFPKM transformations

	Perform the zFPKM transform on RNA-seq FPKM data. This algorithm is based on the publication by Hart et al., 2013 (Pubmed ID 24215113). Reference recommends using zFPKM > -3 to select expressed genes. Validated with encode open/closed chromosome data. Works well for gene level data using FPKM or TPM. Does not appear to calibrate well for transcript level data.
	"""
	
	homepage = "https://github.com/ronammar/zFPKM/"
	bioc = "zFPKM"

	version("1.30.0", commit="8e64f8cc6f79ea411a1aa4b2af4edb4e7435da2d")
	version("1.24.0", commit="631a60f975d89479a64b8b348f56258a70971f64")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
