# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThreeway(RPackage):
	"""Three-Way Component Analysis

	Component analysis for three-way data arrays by means of Candecomp/Parafac, Tucker3, Tucker2 and Tucker1 models.
	"""
	
	cran = "ThreeWay" 

	version("1.1.3", md5="02f38a918a01b413169227062ca25c01")

	depends_on("r@2.8.1:", type=("build", "run"))
