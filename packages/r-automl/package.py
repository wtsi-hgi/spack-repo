# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutoml(RPackage):
	"""Deep Learning with Metaheuristic

	Fits from simple regression to highly customizable deep neural networks 
    either with gradient descent or metaheuristic, using automatic hyper parameters 
    tuning and custom cost function.
    A mix inspired by the common tricks on Deep Learning and Particle Swarm Optimization.
	"""
	
	homepage = "https://aboulaboul.github.io/automl"
	cran = "automl" 

	version("1.3.2", md5="eb498dbd5e5622fe53d0e772593937b0")

