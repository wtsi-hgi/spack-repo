# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbhc(RPackage):
	"""Sequence Clustering with Discrete-Output HMMs

	Provides an implementation of a mixture of hidden Markov models 
    (HMMs) for discrete sequence data in the Discrete Bayesian HMM Clustering 
    (DBHC) algorithm. The DBHC algorithm is an HMM Clustering 
    algorithm that finds a mixture of discrete-output HMMs while using 
    heuristics based on Bayesian Information Criterion (BIC) to search for the 
    optimal number of HMM states and the optimal number of clusters. 
	"""
	
	homepage = "https://github.com/gabybudel/DBHC"
	cran = "DBHC" 

	version("0.0.3", md5="afd1d7b58aeec02211ccac58f6158ba9")

	depends_on("r-seqhmm@1.0.8:", type=("build", "run"))
	depends_on("r-traminer@2.0.7:", type=("build", "run"))
	depends_on("r-reshape2@1.2.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
