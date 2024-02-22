# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClarabel(RPackage):
	"""Interior Point Conic Optimization Solver

	A versatile interior point solver that solves linear programs (LPs), quadratic programs (QPs), second-order cone programs (SOCPs), semidefinite programs (SDPs), and problems with exponential and power cone constraints (<https://oxfordcontrol.github.io/ClarabelDocs/stable/>). For quadratic objectives, unlike interior point solvers based on the standard homogeneous self-dual embedding (HSDE) model, 'Clarabel' handles quadratic objective without requiring any epigraphical reformulation of its objective function. It can therefore be significantly faster than other HSDE-based solvers for problems with quadratic objective functions. Infeasible problems are detected using using a homogeneous embedding technique.
	"""
	
	homepage = "https://oxfordcontrol.github.io/clarabel-r/"
	cran = "clarabel" 

	version("0.5.1", md5="7d0a7e301c11ec5d293b60a5c5eda5c3")

	depends_on("rust", type=("build", "link", "run"))
