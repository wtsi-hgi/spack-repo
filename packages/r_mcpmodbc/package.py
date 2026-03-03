# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcpmodbc(RPackage):
	"""Improved Inference in Multiple Comparison Procedure – Modelling

	Implementation of Multiple Comparison Procedures with Modeling
	(MCP-Mod) procedure with bias-corrected estimators and second-order 
	covariance matrices as described in Diniz, Gallardo and Magalhaes (2023) 
	<doi:10.1002/pst.2303>.
	"""
	
	cran = "MCPModBC" 

	version("1.1", md5="e4e63a96fc5f92c5f39bdee0d7c436f9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dosefinding", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
