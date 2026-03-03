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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pogos_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pogos/pogos_1.22.0.tar.gz"]

	version("1.22.0", md5="14955bb127999aaa92633bc1ce3a1227")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rjson@0.2.15:", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ontoproc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
