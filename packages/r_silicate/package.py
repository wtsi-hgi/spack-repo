# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSilicate(RPackage):
	"""Common Forms for Complex Hierarchical and Relational Data
Structures

	Generate common data forms for complex data suitable for conversions and
 transmission by decomposition as paths or primitives. Paths are sequentially-linked records, 
 primitives are basic atomic elements and both can model many forms and be grouped into hierarchical 
 structures.  The universal models 'SC0' (structural) and 'SC' (labelled, relational) are composed of 
 edges and can represent any hierarchical form. Specialist models 'PATH', 'ARC' and 'TRI' provide the 
 most common intermediate forms used for converting from one form to another. The methods are
 inspired by the simplicial complex <https://en.wikipedia.org/wiki/Simplicial_complex> and 
 provide intermediate forms that relate spatial data structures to this mathematical construct. 
	"""
	
	homepage = "https://github.com/hypertidy/silicate"
	cran = "silicate" 

	version("0.7.1", md5="dede34db423e1867f8fa77e0be64907a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gibble@0.4:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-decido", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-unjoin@0.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-crsmeta@0.3:", type=("build", "run"))
