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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SwathXtend_2.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SwathXtend/SwathXtend_2.24.0.tar.gz"]

	version("2.24.0", sha256="15b633cdf46a51d1eb918f34c5f816bde09a356c91eee6cf30caaad5e11d9b3b")

	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
