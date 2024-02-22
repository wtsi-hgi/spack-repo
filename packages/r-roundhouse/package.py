# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoundhouse(RPackage):
	"""Random Chuck Norris Facts

	R functions for generating and/or displaying random Chuck Norris 
  facts. Based on data from the 'Internet Chuck Norris database' ('ICNDb').
	"""
	
	homepage = "https://github.com/bgreenwell/roundhouse"
	cran = "roundhouse" 

	version("0.0.2", md5="b7d44605e7268c515f9cea39ab7fa392")

