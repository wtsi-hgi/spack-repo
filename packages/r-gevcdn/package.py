# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGevcdn(RPackage):
	"""GEV Conditional Density Estimation Network

	Implements a flexible nonlinear modelling framework for nonstationary generalized extreme value analysis in hydroclimatology following Cannon (2010) <doi:10.1002/hyp.7506>.
	"""
	
	cran = "GEVcdn" 

	version("1.1.6-2", md5="8d8e0b6a513373312b6a0dde81f32893")

