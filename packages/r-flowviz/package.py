# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowviz(RPackage):
	"""Visualization for flow cytometry

	Provides visualization tools for flow cytometry data.
	"""
	
	bioc = "flowViz" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowViz_1.66.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowViz/flowViz_1.66.0.tar.gz"]

	version("1.66.0", md5="320d8392618efe06e6c2a8923b3c6652")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-idpmisc", type=("build", "run"))
