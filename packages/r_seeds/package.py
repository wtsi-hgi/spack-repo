# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeeds(RPackage):
	"""Estimate Hidden Inputs using the Dynamic Elastic Net

	Algorithms to calculate the hidden inputs of systems of differential equations. 
  These hidden inputs can be interpreted as a control that tries to minimize the
  discrepancies between a given model and taken measurements. The idea is 
  also called the Dynamic Elastic Net, as proposed in the paper "Learning (from) the errors of a systems biology model" 
  (Engelhardt, Froelich, Kschischo 2016) <doi:10.1038/srep20772>.
  To use the experimental SBML import function, the 'rsbml' package is required. For installation I refer to the official 'rsbml' page: <https://bioconductor.org/packages/release/bioc/html/rsbml.html>.
	"""
	
	homepage = "https://github.com/Newmi1988/seeds"
	cran = "seeds" 

	version("0.9.1", md5="82c46b7fc967a1240c1ee76499c887a0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-desolve@1.20:", type=("build", "run"))
	depends_on("r-pracma@2.1.4:", type=("build", "run"))
	depends_on("r-deriv@3.8.4:", type=("build", "run"))
	depends_on("r-ryacas", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
