# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReinforcementlearning(RPackage):
	"""Model-Free Reinforcement Learning

	Performs model-free reinforcement learning in R. This implementation enables the learning
    of an optimal policy based on sample sequences consisting of states, actions and rewards. In 
    addition, it supplies multiple predefined reinforcement learning algorithms, such as experience 
    replay. Methodological details can be found in Sutton and Barto (1998) <ISBN:0262039249>.
	"""
	
	cran = "ReinforcementLearning" 

	version("1.0.5", md5="ff5629e28e9c9116d2831aa955cbff09")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hash@2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
