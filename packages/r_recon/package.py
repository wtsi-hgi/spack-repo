# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecon(RPackage):
	"""Computational Tools for Economics

	Implements solutions to canonical models of Economics such as Monopoly Profit Maximization, Cournot's Duopoly, Solow (1956, <doi:10.2307/1884513>) growth model and Mankiw, Romer and Weil (1992, <doi:10.2307/2118477>) growth model.
	"""
	
	cran = "Recon" 

	version("0.3.0.0", md5="3d48c7dd423998cac79decaebd1d69c6")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
