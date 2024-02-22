# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigmelon(RPackage):
	"""Illumina methylation array analysis for large experiments

	Methods for working with Illumina arrays using gdsfmt.
	"""
	
	bioc = "bigmelon" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/bigmelon_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/bigmelon/bigmelon_1.28.0.tar.gz"]

	version("1.28.0", md5="1c6944989ec4f16b1903143a34296bf0")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-watermelon@1.25:", type=("build", "run"))
	depends_on("r-gdsfmt@1.0.4:", type=("build", "run"))
	depends_on("r-minfi@1.21:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-methylumi", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-illuminaio", type=("build", "run"))
