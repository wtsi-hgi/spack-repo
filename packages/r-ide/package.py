# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIde(RPackage):
	"""Integro-Difference Equation Spatio-Temporal Models

	The Integro-Difference Equation model is a linear, dynamical model used to model
   phenomena that evolve in space and in time; see, for example, Cressie and Wikle (2011,
   ISBN:978-0-471-69274-4) or Dewar et al. (2009) <doi:10.1109/TSP.2008.2005091>. At the
   heart of the model is the kernel, which dictates how the process evolves from one time
   point to the next. Both process and parameter reduction are used to facilitate computation,
   and spatially-varying kernels are allowed. Data used to estimate the parameters are assumed
   to be readings of the process corrupted by Gaussian measurement error. Parameters are fitted
   by maximum likelihood, and estimation is carried out using an evolution algorithm. 
	"""
	
	cran = "IDE" 

	version("0.3.1", md5="8e12d351d52e91fd5519820665b05528")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spacetime", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-frk", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-sparseinv", type=("build", "run"))
