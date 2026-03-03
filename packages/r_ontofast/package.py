# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROntofast(RPackage):
	"""Interactive Annotation of Characters with Biological Ontologies

	Tools for annotating characters (character matrices) with anatomical and phenotype ontologies. Includes functions for visualising character annotations and creating simple queries using ontological relationships.
	"""
	
	homepage = "https://github.com/sergeitarasov/ontoFAST"
	cran = "ontoFAST" 

	version("1.0.0", md5="fa1d7a2619722f1f1c96be6775651af3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ontologyindex", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-sunburstr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
