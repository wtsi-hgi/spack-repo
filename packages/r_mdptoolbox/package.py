# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdptoolbox(RPackage):
	"""Markov Decision Processes Toolbox

	The Markov Decision Processes (MDP) toolbox proposes functions related to the resolution of discrete-time Markov Decision Processes: finite horizon, value iteration, policy iteration, linear programming algorithms with some variants and also proposes some functions related to Reinforcement Learning.
	"""
	
	cran = "MDPtoolbox" 

	version("4.0.3", md5="3dd1ea2f1325d24991bd9b4e4b9ca1f7")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-linprog", type=("build", "run"))
