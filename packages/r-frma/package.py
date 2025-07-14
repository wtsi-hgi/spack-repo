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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/frma_1.54.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/frma/frma_1.54.0.tar.gz"]

	version("1.60.0", tag="RELEASE_3_21")
	version("1.54.0", sha256="272d93b320e8293f6d6690926c8968f39cd3b1794e9bbda0e51474a811292d54")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-oligo", type=("build", "run"))
	depends_on("r-oligoclasses", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
