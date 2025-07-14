# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCgen(RPackage):
	"""An R package for analysis of case-control studies in genetic epidemiology

	This is a package for analysis of case-control data in genetic epidemiology. It provides a set of statistical methods for evaluating gene-environment (or gene-genes) interactions under multiplicative and additive risk models, with or without assuming gene-environment (or gene-gene) independence in the underlying population.
	"""
	
	bioc = "CGEN" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CGEN_3.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CGEN/CGEN_3.38.0.tar.gz"]

	version("3.44.0", tag="RELEASE_3_21")
	version("3.38.0", sha256="3609d6ff835c871cbcc497f1e846c6aede3e2d916fe7c6eb14701a313fef5e14")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
