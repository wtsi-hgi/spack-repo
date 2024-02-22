# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHiddenmarkov(RPackage):
	"""Hidden Markov Models

	Contains functions for the analysis of Discrete Time Hidden Markov Models, Markov Modulated GLMs and the Markov Modulated Poisson Process. It includes functions for simulation, parameter estimation, and the Viterbi algorithm. See the topic "HiddenMarkov" for an introduction to the package, and "Change Log" for a list of recent changes. The algorithms are based of those of Walter Zucchini.
	"""
	
	homepage = "https://www.statsresearch.co.nz/dsh/sslib/"
	cran = "HiddenMarkov" 

	version("1.8-13", md5="6ee706a6f6a95ef1fab017ff9d1c7f3b")

