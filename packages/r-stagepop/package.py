# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStagepop(RPackage):
	"""Modelling the Population Dynamics of a Stage-Structured Species
in Continuous Time

	Provides facilities to implement and run population models of
    stage-structured species...
	"""
	
	homepage = "https://github.com/HelenKettle/StagePop"
	cran = "stagePop" 

	version("1.1-2", md5="3ff11fd7fa57dc415c397abc32c18f04")

	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-pbsddesolve", type=("build", "run"))
