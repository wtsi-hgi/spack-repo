# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSra(RPackage):
	"""Selection Response Analysis

	Artificial selection through selective breeding is an efficient way to induce changes in traits of interest in experimental populations. This package (sra) provides a set of tools to analyse artificial-selection response datasets. The data typically feature for several generations the average value of a trait in a population, the variance of the trait, the population size and the average value of the parents that were chosen to breed. Sra implements two families of models aiming at describing the dynamics of the genetic architecture of the trait during the selection response. The first family relies on purely descriptive (phenomenological) models, based on an autoregressive framework. The second family provides different mechanistic models, accounting e.g. for inbreeding, mutations, genetic and environmental canalization, or epistasis. The parameters underlying the dynamics of the time series are estimated by maximum likelihood. The sra package thus provides (i) a wrapper for the R functions mle() and optim() aiming at fitting in a convenient way a predetermined set of models, and (ii) some functions to plot and analyze the output of the models. 
	"""
	
	homepage = "https://github.com/lerouzic/sra"
	cran = "sra" 

	version("0.1.4.1", md5="3f952cc41b7a2f424e8876a4dff857d9")

