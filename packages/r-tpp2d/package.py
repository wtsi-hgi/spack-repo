# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTpp2d(RPackage):
	"""Detection of ligand-protein interactions from 2D thermal profiles (DLPTP)

	Detection of ligand-protein interactions from 2D thermal profiles (DLPTP), Performs an FDR-controlled analysis of 2D-TPP experiments by functional analysis of dose-response curves across temperatures.
	"""
	
	homepage = "http://bioconductor.org/packages/TPP2D"
	bioc = "TPP2D" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TPP2D_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TPP2D/TPP2D_1.18.0.tar.gz"]

	version("1.18.0", sha256="cea550884f057280a2f965b51c305d78d877cfbfeb79d2ed6a6fa5343f194e45")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
