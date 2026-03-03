# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetmix(RPackage):
	"""Dynamic Mixed-Membership Network Regression Model

	Stochastic collapsed variational inference on mixed-membership stochastic blockmodel for networks,
             incorporating node-level predictors of mixed-membership vectors, as well as 
             dyad-level predictors. For networks observed over time, the model defines a hidden
             Markov process that allows the effects of node-level predictors to evolve in discrete,
             historical periods. In addition, the package offers a variety of utilities for 
             exploring results of estimation, including tools for conducting posterior 
             predictive checks of goodness-of-fit and several plotting functions. The package 
             implements methods described in Olivella, Pratt and Imai (2019) 'Dynamic Stochastic
             Blockmodel Regression for Social Networks: Application to International Conflicts',
             available at <https://www.santiagoolivella.info/pdfs/socnet.pdf>.
	"""
	
	cran = "NetMix" 

	version("0.2.0.2", md5="1ff0101f0dabbbf45098659e59b9807a")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-clue@0.3.58:", type=("build", "run"))
	depends_on("r-gtools@3.8.1:", type=("build", "run"))
	depends_on("r-igraph@1.2.4.1:", type=("build", "run"))
	depends_on("r-lda@1.4.2:", type=("build", "run"))
	depends_on("r-matrix@1.2.15:", type=("build", "run"))
	depends_on("r-mass@7.3.51.4:", type=("build", "run"))
	depends_on("r-poisbinom@1.0.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
