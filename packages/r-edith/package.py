# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdith(RPackage):
	"""Model Transport of Environmental DNA in River Networks

	Runs the eDITH (environmental DNA Integrating Transport 
  and Hydrology) model, which implements a mass balance of environmental DNA (eDNA) 
  transport at a river network scale coupled with a species distribution model 
  to obtain maps of species distribution. eDITH can work with both eDNA concentration 
  (e.g., obtained via quantitative polymerase chain reaction) or metabarcoding 
  (read count) data. Parameter estimation can be performed via Bayesian techniques 
  (via the 'BayesianTools' package) or optimization algorithms. An interface to the 
  'DHARMa' package for posterior predictive checks is provided. See Carraro and 
  Altermatt (2024) <doi:10.1111/2041-210X.14317> for a package introduction; 
  Carraro et al. (2018) <doi:10.1073/pnas.1813843115> and Carraro et al. (2020) 
  <doi:10.1038/s41467-020-17337-8> for methodological details. 
	"""
	
	homepage = "https://lucarraro.github.io/eDITH/"
	cran = "eDITH" 

	version("0.2.0", md5="4e90c2ef95b3f6c85a6ca5cf3cf9dacb")
	version("0.3.0", md5="27a67923390d3a99f36e148245c611c4")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ocnet@1.1:", type=("build", "run"))
	depends_on("r-rivnet@0.3.1:", type=("build", "run"))
	depends_on("r-bayesiantools", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-dharma", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
