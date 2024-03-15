# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsimsum(RPackage):
	"""Analysis of Simulation Studies Including Monte Carlo Error

	Summarise results from simulation studies and compute Monte Carlo
  standard errors of commonly used summary statistics. This package is modelled 
  on the 'simsum' user-written command in 'Stata' (White I.R., 2010 
  <https://www.stata-journal.com/article.html?article=st0200>), further extending
  it with additional performance measures and functionality.
	"""
	
	homepage = "https://ellessenne.github.io/rsimsum/"
	cran = "rsimsum" 

	version("0.13.0", md5="3baf3c8ed456270ec3093b085f022a06")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
