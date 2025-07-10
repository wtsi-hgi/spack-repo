# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSquadd(RPackage):
	"""Add-on of the SQUAD Software

	This package SQUADD is a SQUAD add-on. It permits to generate SQUAD simulation matrix, prediction Heat-Map and Correlation Circle from PCA analysis.
	"""
	
	homepage = "http://www.unil.ch/dbmv/page21142_en.html"
	bioc = "SQUADD" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SQUADD_1.52.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SQUADD/SQUADD_1.52.0.tar.gz"]

	version("1.52.0", sha256="064abffe42d9c6ce0e64bd8e702b9d5c7a39a64793f8d7e428b351253aace76d")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
