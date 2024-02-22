# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtr(RPackage):
	"""Alternative Tree Representation

	Plot party trees in left-right orientation instead of the
  classical top-down layout.
	"""
	
	cran = "ATR" 

	version("0.1-1", md5="0d255c506b8c811fa9ec8128aa22a73d")

	depends_on("r-partykit", type=("build", "run"))
