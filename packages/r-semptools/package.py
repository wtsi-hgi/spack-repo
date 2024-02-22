# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemptools(RPackage):
	"""Customizing Structural Equation Modelling Plots

	Most function focus on specific ways to customize a graph.
             They use a 'qgraph' output  as the first argument, and return a
             modified 'qgraph' object. This allows the functions to be chained
             by a pipe operator.
	"""
	
	homepage = "https://sfcheung.github.io/semptools/"
	cran = "semptools" 

	version("0.2.10", md5="6cde52398708908cd9e6777fe77041da")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-semplot", type=("build", "run"))
