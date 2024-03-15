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

	version("1.52.0", md5="8837e27ab065ddae145da3cc5ca2ad32")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
