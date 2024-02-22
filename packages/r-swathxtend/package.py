# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwathxtend(RPackage):
	"""SWATH extended library generation and statistical data analysis

	Contains utility functions for integrating spectral libraries for SWATH and statistical data analysis for SWATH generated data.
	"""
	
	bioc = "SwathXtend" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SwathXtend_2.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SwathXtend/SwathXtend_2.24.0.tar.gz"]

	version("2.24.0", md5="64b04f78ca92078b9ad63cee65bf012f")

	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
