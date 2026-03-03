# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnrepx(RPackage):
	"""Analysis and Graphics for Unreplicated Experiments

	Provides half-normal plots, reference plots, and Pareto plots
    of effects from an unreplicated experiment, along with various 
    pseudo-standard-error measures, simulated reference distributions, 
    and other tools. Many of these methods are described in 
    Daniel C. (1959) <doi:10.1080/00401706.1959.10489866> and/or
    Lenth R.V. (1989) <doi:10.1080/00401706.1989.10488595>, but some new
    approaches are added and integrated in one package.
	"""
	
	cran = "unrepx" 

	version("1.0-2", md5="70ded5fddba6c9f695a7acba2a175417")

