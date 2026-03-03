# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMtdrh(RPackage):
	"""Mass Transportation Distance Rank Histogram

	The Mass Transportation Distance rank histogram was developed to assess the reliability of scenarios with equal or different probabilities of occurrence <doi:10.1002/we.1872>.
	"""
	
	cran = "MTDrh" 

	version("0.1.0", md5="83e43ac001693e26312eb63a1330b1d2")

