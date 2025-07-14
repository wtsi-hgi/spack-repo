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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/curatedTBData_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/curatedTBData/curatedTBData_1.8.0.tar.gz"]

	version("2.4.0", tag="RELEASE_3_21")
	version("1.8.0", sha256="1a675f4a41186e1144bb83134b84e1a521772eeaa01b31228db1197e8399cc84")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))

