# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixsim(RPackage):
	"""Simulating Data to Study Performance of Clustering Algorithms

	The utility of this package is in simulating mixtures of Gaussian
        distributions with different levels of overlap between mixture
        components.  Pairwise overlap, defined as a sum of two
        misclassification probabilities, measures the degree of
        interaction between components and can be readily employed to
        control the clustering complexity of datasets simulated from
        mixtures. These datasets can then be used for systematic
        performance investigation of clustering and finite mixture
        modeling algorithms. Among other capabilities of 'MixSim', there
        are computing the exact overlap for Gaussian mixtures,
        simulating Gaussian and non-Gaussian data, simulating outliers
        and noise variables, calculating various measures of agreement
        between two partitionings, and constructing parallel
        distribution plots for the graphical display of finite mixture
        models.
	"""
	
	cran = "MixSim" 

	version("1.1-7", md5="6c613ea317c1de8123b0a4d485e1ec56")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
