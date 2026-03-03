# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCge(RPackage):
	"""Computing General Equilibrium

	Developing general equilibrium models, computing general equilibrium and simulating economic dynamics with structural dynamic models in LI (2019, ISBN: 9787521804225) "General Equilibrium and Structural Dynamics: Perspectives of New Structural Economics. Beijing: Economic Science Press". When developing complex general equilibrium models, GE package should be used in addition to this package.
	"""
	
	cran = "CGE" 

	version("0.3.3", md5="259a5531f76f6597d3d23f7fc5fb9555")

