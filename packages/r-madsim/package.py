# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMadsim(RPackage):
	"""A Flexible Microarray Data Simulation Model

	This function allows to generate two biological conditions synthetic 
             microarray dataset which has similar behavior to those currently 
             observed with common platforms. User provides a subset of parameters.
             Available default parameters settings can be modified.
	"""
	
	cran = "madsim" 

	version("1.2.1", md5="37821028eb84c018643b9ad9ef583f91")

