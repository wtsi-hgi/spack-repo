# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetcirc(RPackage):
	"""Navigating mass spectral similarity in high-resolution MS/MS metabolomics data metabolomics data

	MetCirc comprises a workflow to interactively explore high-resolution MS/MS metabolomics data. MetCirc uses the Spectra object infrastructure defined in the package Spectra that stores MS/MS spectra. MetCirc offers functionality to calculate similarity between precursors based on the normalised dot product, neutral losses or user-defined functions and visualise similarities in a circular layout. Within the interactive framework the user can annotate MS/MS features based on their similarity to (known) related MS/MS features.
	"""
	
	bioc = "MetCirc" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MetCirc_1.32.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MetCirc/MetCirc_1.32.0.tar.gz"]

	version("1.32.0", md5="c21a385245acf6911f5c762093ea6e0b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-amap@0.8:", type=("build", "run"))
	depends_on("r-circlize@0.3.9:", type=("build", "run"))
	depends_on("r-scales@0.3:", type=("build", "run"))
	depends_on("r-shiny@1:", type=("build", "run"))
	depends_on("r-spectra@1.4.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-mscoreutils@1.9.2:", type=("build", "run"))
	depends_on("r-s4vectors@0.22:", type=("build", "run"))
