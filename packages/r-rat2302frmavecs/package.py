# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRat2302frmavecs(RPackage):
	"""Vectors used by frma for microarrays of type rat2302rnentrezg

	This package was created with the help of frmaTools version 1.24.0.
	"""
	
	bioc = "rat2302frmavecs" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rat2302frmavecs_0.99.11.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rat2302frmavecs/rat2302frmavecs_0.99.11.tar.gz"]

	version("0.99.11", sha256="3186bc3b19f48b1da4dacaafbf34c4804997389b8634f33c1076666a9083c563")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-frma", type=("build", "run"))

