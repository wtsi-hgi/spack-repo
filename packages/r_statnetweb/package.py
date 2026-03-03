# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatnetweb(RPackage):
	"""A Graphical User Interface for Network Modeling with 'Statnet'

	A graphical user interface for network modeling with the 'statnet'
    software <https://github.com/statnet>.
	"""
	
	cran = "statnetWeb" 

	version("0.5.6", md5="1e270b8e6d3d835ce5e0a2085840cd29")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny@1.3:", type=("build", "run"))
	depends_on("r-ergm@3.10.4:", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
