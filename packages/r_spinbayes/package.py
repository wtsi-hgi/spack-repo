# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpinbayes(RPackage):
	"""Semi-Parametric Gene-Environment Interaction via Bayesian
Variable Selection

	Many complex diseases are known to be affected by the interactions between 
   genetic variants and environmental exposures beyond the main genetic and environmental 
   effects. Existing Bayesian methods for gene-environment (G×E) interaction studies are 
   challenged by the high-dimensional nature of the study and the complexity of environmental 
   influences. We have developed a novel and powerful semi-parametric Bayesian variable 
   selection method that can accommodate linear and nonlinear G×E interactions simultaneously 
   (Ren et al. (2020) <doi:10.1002/sim.8434>). Furthermore, the proposed method can conduct 
   structural identification by distinguishing nonlinear interactions from main effects only 
   case within Bayesian framework. Spike-and-slab priors are incorporated on both individual 
   and group level to shrink coefficients corresponding to irrelevant main and interaction 
   effects to zero exactly. The Markov chain Monte Carlo algorithms of the proposed and 
   alternative methods are  efficiently implemented in C++. 
	"""
	
	homepage = "https://github.com/jrhub/spinBayes"
	cran = "spinBayes" 

	version("0.2.1", md5="6bb865aed0f5562a4efdbf154456554e")
	version("0.1.0", md5="660825909018c3cb5b12901a8f77dfa2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
