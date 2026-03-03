# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNoisysbm(RPackage):
	"""Noisy Stochastic Block Mode: Graph Inference by Multiple Testing

	Variational Expectation-Maximization algorithm to fit the noisy stochastic block model to an observed dense graph 
    and to perform a node clustering. Moreover, a graph inference procedure to recover the underlying 
    binary graph. This procedure comes with a control of the false discovery rate. The method is described
    in the article "Powerful graph inference with false discovery rate control" by T. Rebafka, 
    E. Roquain, F. Villers (2020) <arXiv:1907.10176>.
	"""
	
	cran = "noisySBM" 

	version("0.1.4", md5="83fb9b275ea27591400d5af3b5647a55")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
