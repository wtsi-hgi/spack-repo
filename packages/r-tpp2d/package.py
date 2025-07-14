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

	version("1.24.0", commit="7f0e386df9727e1d2bad8f0813535112aeff89ba")
	version("1.18.0", commit="f78c9fc90ca003fa6849393b86108d17594ba398")

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
