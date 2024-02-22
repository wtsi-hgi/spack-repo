# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPreprocessing(RPackage):
	"""Various Preprocessing Transformations of Numeric Data Matrices

	Preprocess numeric data matrices into desired transformed representations.
    Standardization, Unitization, Cubitization and adaptive intervals are offered.
	"""
	
	cran = "PreProcessing" 

	version("0.1.0", md5="a3e4bf7163444f4243b708bd7bcc5f5c")

	depends_on("r-ggplot2@1.0.1:", type=("build", "run"))
