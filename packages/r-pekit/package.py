# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPekit(RPackage):
	"""Partition Exchangeability Toolkit

	Bayesian supervised predictive classifiers, hypothesis testing, and parametric estimation under Partition Exchangeability are implemented. The two classifiers presented are the marginal classifier (that assumes test data is i.i.d.) next to a more computationally costly but accurate simultaneous classifier (that finds a labelling for the entire test dataset at once based on simultanous use of all the test data to predict each label). We also provide the Maximum Likelihood Estimation (MLE) of the only underlying parameter of the partition exchangeability generative model as well as hypothesis testing statistics for equality of this parameter with a single value, alternative, or multiple samples. We present functions to simulate the sequences from Ewens Sampling Formula as the realisation of the Poisson-Dirichlet distribution and their respective probabilities.
	"""
	
	cran = "PEkit" 

	version("1.0.0.1000", md5="b3e75f0a6c86c8e8f758146f3ee9c378")

