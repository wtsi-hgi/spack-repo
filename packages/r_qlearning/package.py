# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQlearning(RPackage):
	"""Reinforcement Learning using the Q Learning Algorithm

	Implements Q-Learning, a model-free form of reinforcement
        learning, described in work by Strehl, Li, Wiewiora, Langford &
        Littman (2006) <doi:10.1145/1143844.1143955>.
	"""
	
	cran = "QLearning" 

	version("0.1.1", md5="8a7c00b82a0c9b8ab86b2b5352187dc2")

