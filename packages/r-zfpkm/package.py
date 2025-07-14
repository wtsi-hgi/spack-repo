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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/zFPKM_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/zFPKM/zFPKM_1.24.0.tar.gz"]

	version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="84a079537a04b4f8c33986ee8f2d0e891eff461e886e05edf5819e1c0afbf6a2")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
