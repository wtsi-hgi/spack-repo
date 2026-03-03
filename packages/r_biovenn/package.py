# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiovenn(RPackage):
	"""Create Area-Proportional Venn Diagrams from Biological Lists

	Creates an area-proportional Venn diagram of 2 or 3 circles. 'BioVenn' is the only R package that can automatically generate an accurate area-proportional Venn diagram by having only lists of (biological) identifiers as input. Also offers the option to map Entrez and/or Affymetrix IDs to Ensembl IDs. In SVG mode, text and numbers can be dragged and dropped. Based on the BioVenn web interface available at <https://www.biovenn.nl>. Hulsen (2021) <doi:10.3233/DS-210032>.
	"""
	
	cran = "BioVenn" 

	version("1.1.3", md5="82440f0517815c06415b753dc3b424ee")

	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-svglite", type=("build", "run"))
