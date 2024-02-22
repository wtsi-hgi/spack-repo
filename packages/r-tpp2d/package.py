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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/TPP2D_1.18.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/TPP2D/TPP2D_1.18.0.tar.gz"]

	version("1.18.0", md5="b10330822e1c629c04c568ab155b4ee1")

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
