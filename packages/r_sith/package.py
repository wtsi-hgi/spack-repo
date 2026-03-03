# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSith(RPackage):
	"""A Spatial Model of Intra-Tumor Heterogeneity

	Implements a three-dimensional stochastic model of cancer growth and mutation similar to the one described in Waclaw et al. (2015) <doi:10.1038/nature14971>. Allows for interactive 3D visualizations of the simulated tumor. Provides a comprehensive summary of the spatial distribution of mutants within the tumor. Contains functions which create synthetic sequencing datasets from the generated tumor. 
	"""
	
	homepage = "https://github.com/phillipnicol/SITH"
	cran = "SITH" 

	version("1.1.0", md5="4be5c8f4bdbde6f02774d676813c1719")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
