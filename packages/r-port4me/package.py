# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPort4me(RPackage):
	"""Get the Same, Personal, Free 'TCP' Port over and over

	An R implementation of the cross-platform, language-independent "port4me" algorithm (<https://github.com/HenrikBengtsson/port4me>), which (1) finds a free Transmission Control Protocol ('TCP') port in [1024,65535] that the user can open, (2) is designed to work in multi-user environments, (3), gives different users, different ports, (4) gives the user the same port over time with high probability, (5) gives different ports for different software tools, and (6) requires no configuration.
	"""
	
	homepage = "https://github.com/HenrikBengtsson/port4me"
	cran = "port4me" 

	version("0.7.1", md5="010d84686f7f81b31e896730a0168f37")

