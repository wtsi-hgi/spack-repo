# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROompabase(RPackage):
	"""Class Unions, Matrix Operations, and Color Schemes for OOMPA

	Provides the class unions that must be
  preloaded in order for the basic tools in the OOMPA (Object-Oriented 
  Microarray and Proteomics Analysis) project to be defined and loaded.
  It also includes vectorized operations for row-by-row means,
  variances, and t-tests. Finally, it provides new color schemes.
  Details on the packages in the OOMPA project can be found at
  <http://oompa.r-forge.r-project.org/>.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "oompaBase" 

	version("3.2.9", md5="e4697828589889278211385df36c0dcc")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
