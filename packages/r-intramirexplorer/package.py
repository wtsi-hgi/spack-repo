# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntramirexplorer(RPackage):
	"""Predicting Targets for Drosophila Intragenic miRNAs

	Intra-miR-ExploreR, an integrative miRNA target prediction bioinformatics tool, identifies targets combining expression and biophysical interactions of a given microRNA (miR). Using the tool, we have identified targets for 92 intragenic miRs in D. melanogaster, using available microarray expression data, from Affymetrix 1 and Affymetrix2 microarray array platforms, providing a global perspective of intragenic miR targets in Drosophila. Predicted targets are grouped according to biological functions using the DAVID Gene Ontology tool and are ranked based on a biologically relevant scoring system, enabling the user to identify functionally relevant targets for a given miR.
	"""
	
	homepage = "https://github.com/VilainLab/IntramiRExploreR"
	bioc = "IntramiRExploreR"

	version("1.30.0", commit="ea62cbd36d703936cd9c9b133d57facd1ebba4a0")
	version("1.24.0", commit="72598bd0cbc119da9f47d2ad4b5a40ffbec5ba1c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-fgnet@3.0.7:", type=("build", "run"))
	depends_on("r-knitr@1.12.3:", type=("build", "run"))
