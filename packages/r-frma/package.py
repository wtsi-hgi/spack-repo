# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrma(RPackage):
	"""Frozen RMA and Barcode

	Preprocessing and analysis for single microarrays and microarray batches.
	"""
	
	homepage = "http://bioconductor.org"
	bioc = "frma"

	version("1.60.0", commit="19367807be1719dcfaf03b1b88b046a31d4da691")
	version("1.54.0", commit="6bdb804c2c60f62b2f5da77678d2aaee9e2a4d11")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-oligo", type=("build", "run"))
	depends_on("r-oligoclasses", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
