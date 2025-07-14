# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPogos(RPackage):
	"""PharmacOGenomics Ontology Support

	Provide simple utilities for querying bhklab PharmacoDB, modeling API outputs, and integrating to cell and compound ontologies.
	"""
	
	bioc = "pogos"

	version("1.28.0", commit="5391771a5a5456c610baf10a900508ef4d433205")
	version("1.22.0", commit="7f46f03aa7382a3218ef57b2baa95a0f5cf125da")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rjson@0.2.15:", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ontoproc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
