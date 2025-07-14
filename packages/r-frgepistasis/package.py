# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrgepistasis(RPackage):
	"""Epistasis Analysis for Quantitative Traits by Functional Regression Model

	A Tool for Epistasis Analysis Based on Functional Regression Model
	"""
	
	bioc = "FRGEpistasis" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/FRGEpistasis_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/FRGEpistasis/FRGEpistasis_1.38.0.tar.gz"]

	version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="e23082e26cd4be31092f65682eccca383f16ff9d84b231051bbd6c135248b9e6")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
