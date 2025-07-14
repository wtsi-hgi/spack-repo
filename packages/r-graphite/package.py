# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphite(RPackage):
	"""GRAPH Interaction from pathway Topological Environment

	Graph objects from pathway topology derived from KEGG, Panther, PathBank, PharmGKB, Reactome SMPDB and WikiPathways databases.
	"""
	
	homepage = "https://github.com/sales-lab/graphite"
	bioc = "graphite"

	version("1.54.0", commit="4461304007ebb656aab119580c0f59316de59cc2")
	version("1.48.0", commit="288e32a0bedd7a0c53f54237b725631f7e6d9aa6")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-graph@1.67.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
