# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlattice(RPackage):
	"""Lattice Plot for Panel Data

	It creates a lattice plot to visualize panel or longitudinal data. The observed values are plotted as dots and the fitted values as lines, both against time. The plot is customizable and easy to edit, even if you do not know how to construct a lattice plot from scratch.
	"""
	
	cran = "plattice" 

	version("1.0", md5="f21e123d5be825ccd6c05dd49a6f67a8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
