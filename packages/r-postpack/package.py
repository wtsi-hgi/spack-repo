# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPostpack(RPackage):
	"""Utilities for Processing Posterior Samples Stored in
'mcmc.lists'

	The aim of 'postpack' is to provide the infrastructure for a standardized workflow for 'mcmc.list' objects.
    These objects can be used to store output from models fitted with Bayesian inference using
    'JAGS', 'WinBUGS', 'OpenBUGS', 'NIMBLE', 'Stan', or even custom MCMC algorithms. Although the 'coda' R package provides
    some methods for these objects, it is somewhat limited in easily performing post-processing tasks for
    specific nodes. Models are ever increasing in their complexity and the number of tracked nodes, and oftentimes
    a user may wish to summarize/diagnose sampling behavior for only a small subset of nodes at a time
    for a particular question or figure. Thus, many 'postpack' functions support performing tasks on a
    subset of nodes, where the subset is specified with regular expressions. The functions in 'postpack'
    streamline the extraction, summarization, and diagnostics of specific monitored nodes after model fitting.
    Further, because there is rarely only ever one model under consideration, 'postpack' scales efficiently 
    to perform the same tasks on output from multiple models simultaneously, facilitating rapid assessment 
    of model sensitivity to changes in assumptions.
	"""
	
	homepage = "https://bstaton1.github.io/postpack/"
	cran = "postpack" 

	version("0.5.4", md5="1b1861ca97f725398fbf656ed33a89d5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mcmcse", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
