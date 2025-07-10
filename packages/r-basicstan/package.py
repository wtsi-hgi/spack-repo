# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasicstan(RPackage):
	"""Stan implementation of BASiCS

	Provides an interface to infer the parameters of BASiCS using the variational inference (ADVI), Markov chain Monte Carlo (NUTS), and maximum a posteriori (BFGS) inference engines in the Stan programming language. BASiCS is a Bayesian hierarchical model that uses an adaptive Metropolis within Gibbs sampling scheme. Alternative inference methods provided by Stan may be preferable in some situations, for example for particularly large data or posterior distributions with difficult geometries.
	"""
	
	homepage = "https://github.com/Alanocallaghan/BASiCStan"
	bioc = "BASiCStan" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BASiCStan_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BASiCStan/BASiCStan_1.4.0.tar.gz"]

	version("1.4.0", sha256="3176517994f10d6a9dd9571ae1d51d87e9ef2d5aed81da215b5a195ba516ea06")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-basics", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-glmgampoi", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
	depends_on("r-scuttle", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
