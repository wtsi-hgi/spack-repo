# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBdlp(RPackage):
	"""Transparent and Reproducible Artificial Data Generation

	The main function generateDataset() processes a user-supplied .R file that 
  contains metadata parameters in order to generate actual data. The metadata parameters 
  have to be structured in the form of metadata objects, the format of which is 
  outlined in the package vignette. This approach allows to generate artificial data 
  in a transparent and reproducible manner.
	"""
	
	cran = "bdlp" 

	version("0.9-2", md5="f92305dc44ad3e05a91513bafd138065")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-genord", type=("build", "run"))
	depends_on("r-multiord", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
