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

	version("1.52.0", commit="6b55f47fe9fe8c813f2eaef3cbdc0a4a7f59f64b")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
