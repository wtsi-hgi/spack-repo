# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlaunet(RPackage):
	"""Calculate and Analyze Blau Statuses for Measuring Social
Distance

	Calculate and analyze Blau statuses for quantifying social distance between individuals belonging to organizations. Relational (network) data can be incorporated for additional analyses. This project is supported by Defense Threat Reduction Agency (DTRA) Grant HDTRA-10-1-0043.
	"""
	
	homepage = "https://www.facebook.com/groups/425015561030239/"
	cran = "Blaunet" 

	version("2.2.1", md5="12da0a885c2e6e85890e2a5ff8411e7a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-gwidgets2", type=("build", "run"))
	depends_on("r-gwidgets2tcltk", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-plot3drgl", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-ergm", type=("build", "run"))
	depends_on("r-statnet-common", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
