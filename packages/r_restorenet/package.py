# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRestorenet(RPackage):
	"""Random-Effects Stochastic Reaction Networks

	A random-effects stochastic model that allows quick detection of 
  clonal dominance events from clonal tracking data collected in gene therapy studies. Starting from the Ito-type equation describing the dynamics of cells duplication, death and differentiation at clonal level, we first considered its local linear approximation as the base model. 
  The parameters of the base model, which are inferred using a maximum likelihood approach, 
  are assumed to be shared across the clones. Although this assumption makes inference easier, 
  in some cases it can be too restrictive and does not take into account possible scenarios of clonal dominance. 
  Therefore we extended the base model by introducing random effects for the clones. 
  In this extended formulation the dynamic parameters are estimated using a tailor-made 
  expectation maximization algorithm. Further details on the methods can be found in L. Del Core et al., (2022) <doi:10.1101/2022.05.31.494100>.
	"""
	
	cran = "RestoreNet" 

	version("1.0.1", md5="7add8755f0ff0a4f290f6acff9626919")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scatterpie", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
