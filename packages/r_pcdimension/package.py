# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcdimension(RPackage):
	"""Finding the Number of Significant Principal Components

	Implements methods to automate the Auer-Gervini graphical
  Bayesian approach for determining the number of significant
  principal components. Automation uses clustering, change points, or
  simple statistical models to distinguish "long" from "short" steps
  in a graph showing the posterior number of components as a function
  of a prior parameter. See <doi:10.1101/237883>.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "PCDimension" 

	version("1.1.13", md5="5a0d3e27100fc46bd91bab1cd5ff5ae6")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-classdiscovery", type=("build", "run"))
	depends_on("r-oompabase", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-cpm", type=("build", "run"))
