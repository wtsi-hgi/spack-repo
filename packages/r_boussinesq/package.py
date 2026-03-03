# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoussinesq(RPackage):
	"""Analytic Solutions for (Ground-Water) Boussinesq Equation

	A collection of R functions were implemented
        from published and available analytic solutions for the
        One-Dimensional Boussinesq Equation (ground-water). In
        particular, the function "beq.lin()" is the analytic solution of
        the linearized form of Boussinesq Equation between two
        different head-based boundary (Dirichlet) conditions;
        "beq.song" is the non-linear power-series analytic solution of
        the motion of a wetting front over a dry bedrock (Song at al,
        2007, see complete reference on function documentation).
        Bugs/comments/questions/collaboration of any kind are warmly
        welcomed.
	"""
	
	homepage = "https://github.com/ecor/boussinesq"
	cran = "boussinesq" 

	version("1.0.6", md5="f06719b6585fe006f6eb3334ca24e987")

	depends_on("r@2.10:", type=("build", "run"))
