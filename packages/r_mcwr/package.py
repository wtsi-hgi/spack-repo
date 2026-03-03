# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcwr(RPackage):
	"""Markov Chains with Rewards

	In the context of multistate models, which are popular in sociology,
    demography, and epidemiology, Markov chain with rewards calculations can
    help to refine transition timings and so obtain more accurate estimates. The
    package code accommodates up to nine transient states and irregular age (time)
    intervals. Traditional demographic life tables result as a special case.
    Formulas and methods involved are explained in detail in the accompanying
    article: Schneider / Myrskyla / van Raalte (2021): Flexible Transition Timing
    in Discrete-Time Multistate Life Tables Using Markov Chains with Rewards,
    MPIDR Working Paper WP-2021-002.
	"""
	
	cran = "mcwr" 

	version("1.0.0", md5="bb50638cf5053e7cf8e8dfd07275e130")

	depends_on("r@3.6:", type=("build", "run"))
