# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuint(RPackage):
	"""Qualitative Interaction Trees

	Grows a qualitative interaction tree. Quint is a tool for subgroup analysis, suitable for data from a two-arm randomized controlled trial. More information in Dusseldorp, E., Doove, L., & Van Mechelen, I. (2016) <doi:10.3758/s13428-015-0594-z>.
	"""
	
	cran = "quint" 

	version("2.2.2", md5="298c335af5b66280cb2ab8d9bb17e3b1")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
