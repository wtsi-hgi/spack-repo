# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROntologyindex(RPackage):
	"""Reading Ontologies into R

	Functions for reading ontologies into R as lists and manipulating sets of ontological terms - 'ontologyX: A suite of R packages for working with ontological data', Greene et al 2017 <doi:10.1093/bioinformatics/btw763>.
	"""
	
	cran = "ontologyIndex" 

	version("2.12", md5="ebbcda13ca7f5cf8663769d740b09f0a")
	version("2.11", md5="c252ea80927b096d3a0b8be63263aa11")

	depends_on("r@3.5:", type=("build", "run"))
