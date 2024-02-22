# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGen2stage(RPackage):
	"""Generalized Two-Stage Designs for Phase II Single-Arm Studies

	One can find single-stage and two-stage designs for a phase II 
    single-arm study with either efficacy or safety/toxicity endpoints as described in Kim and Wong (2019) <doi:10.29220/CSAM.2019.26.2.163>. 
	"""
	
	cran = "gen2stage" 

	version("1.0", md5="29383b6302212f44e410fc8918252f38")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-clinfun", type=("build", "run"))
