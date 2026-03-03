# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToolbox(RPackage):
	"""List, String, and Meta Programming Utility Functions

	Includes functions for mapping named lists to function arguments, random strings,
  pasting and combining rows together across columns, etc.
	"""
	
	cran = "toolbox" 

	version("0.1.1", md5="819e9386629f3769fa2a8bafdea1d621")

