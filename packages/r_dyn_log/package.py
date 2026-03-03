# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynLog(RPackage):
	"""Dynamic Logging for R Inspired by Configuration Driven
Development

	A comprehensive and dynamic configuration driven logging package for R. While there 
    are several excellent logging solutions already in the R ecosystem, I always feel constrained 
    in some way by each of them. Every project is designed differently to solve it's domain specific problem, 
    and ultimately the utility of a logging solution is its ability to adapt to this design. This is the 
    raison d'être for 'dyn.log': to provide a modular design, template mechanics and a configuration-based 
    integration model, so that the logger can integrate deeply into your design, even though it knows 
    nothing about it.
	"""
	
	homepage = "https://bmoretz.github.io/dyn.log/"
	cran = "dyn.log" 

	version("0.4.0", md5="e57c4420fbbf895e7fce55513961c5b5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-crayon@1.4.1:", type=("build", "run"))
	depends_on("r-glue@1.4.2:", type=("build", "run"))
	depends_on("r-r6@2.5.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.12:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-yaml@2.2.1:", type=("build", "run"))
