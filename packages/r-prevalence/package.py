# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrevalence(RPackage):
	"""Tools for Prevalence Assessment Studies

	The prevalence package provides Frequentist and Bayesian methods for prevalence assessment studies. IMPORTANT: the truePrev functions in the prevalence package call on JAGS (Just Another Gibbs Sampler), which therefore has to be available on the user's system. JAGS can be downloaded from <https://mcmc-jags.sourceforge.io/>.
	"""
	
	homepage = "http://prevalence.cbra.be/"
	cran = "prevalence" 

	version("0.4.1", md5="da6f4f306a83d4844da5e0505478c897")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("jags@4.0.0:", type=("build", "link", "run"))
