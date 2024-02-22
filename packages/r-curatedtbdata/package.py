# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuratedtbdata(RPackage):
	"""Curation of existing 49 tuberculosis transcriptomic studies

	The curatedTBData is an R package that provides standardized, curated tuberculosis(TB) transcriptomic studies. The initial release of the package contains 49 studies. The curatedTBData package allows users to access tuberculosis trancriptomic efficiently and to make efficient comparison for different TB gene signatures across multiple datasets.
	"""
	
	homepage = "https://github.com/compbiomed/curatedTBData"
	bioc = "curatedTBData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/curatedTBData_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/curatedTBData/curatedTBData_1.8.0.tar.gz"]

	version("1.8.0", md5="190a770c4f5df45cf722b7ee287a2384")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))

	# experiment