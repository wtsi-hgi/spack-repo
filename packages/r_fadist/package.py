# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFadist(RPackage):
	"""Distributions that are Sometimes Used in Hydrology

	Probability distributions that are sometimes useful in hydrology.
	"""
	
	homepage = "https://github.com/tpetzoldt/FAdist"
	cran = "FAdist" 

	version("2.4", md5="a7f13561055d26f9c11da8a494f3caca")

