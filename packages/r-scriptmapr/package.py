# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScriptmapr(RPackage):
	"""R Script Visualization in Cytoscape

	Displays the content of a R script into the 'Cytoscape' network-visualization app <https://cytoscape.org/>.
	"""
	
	cran = "ScriptMapR" 

	version("0.0.3", md5="db7a6e3690a6c84756f58d8a612b134e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcy3", type=("build", "run"))
	depends_on("r-formatr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
