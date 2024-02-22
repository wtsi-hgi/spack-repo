# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrimer(RPackage):
	"""Functions and Data for the Book, a Primer of Ecology with R

	Functions are primarily functions for systems of ordinary differential equations, difference equations, and eigenanalysis and projection of demographic matrices; data are for examples.
	"""
	
	cran = "primer" 

	version("1.2.0", md5="5ad43ce2e649a66ac231b7cc6b1a1b73")

	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@3.10:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
