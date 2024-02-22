# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhosphonormalizer(RPackage):
	"""Compensates for the bias introduced by median normalization in

	It uses the overlap between enriched and non-enriched datasets to compensate for the bias introduced in global phosphorylation after applying median normalization.
	"""
	
	bioc = "phosphonormalizer" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/phosphonormalizer_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/phosphonormalizer/phosphonormalizer_1.26.0.tar.gz"]

	version("1.26.0", md5="b0146ac595b90e20d854404e6fa427bb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
