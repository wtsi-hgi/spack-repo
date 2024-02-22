# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDirichletprocess(RPackage):
	"""Build Dirichlet Process Objects for Bayesian Modelling

	Perform nonparametric Bayesian analysis using Dirichlet 
    processes without the need to program the inference algorithms. 
    Utilise included pre-built models or specify custom 
    models and allow the 'dirichletprocess' package to handle the 
    Markov chain Monte Carlo sampling. 
    Our Dirichlet process objects can act as building blocks for a variety 
    of statistical models including and not limited to: density estimation, 
    clustering and prior distributions in hierarchical models.
    See Teh, Y. W. (2011) 
    <https://www.stats.ox.ac.uk/~teh/research/npbayes/Teh2010a.pdf>, 
    among many other sources.
	"""
	
	homepage = "https://github.com/dm13450/dirichletprocess"
	cran = "dirichletprocess" 

	version("0.4.2", md5="c743fc6a653eb231d204f8bb87df5513")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
