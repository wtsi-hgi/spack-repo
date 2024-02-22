# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVdgraph(RPackage):
	"""Variance Dispersion Graphs and Fraction of Design Space Plots
for Response Surface Designs

	Uses a modification of the published FORTRAN code in "A Computer Program for Generating Variance Dispersion Graphs" by G. Vining, Journal of Quality Technology, Vol. 25 No. 1 January 1993, to produce variance dispersion graphs. Also produces fraction of design space plots, and contains data frames for several minimal run response surface designs. 
	"""
	
	cran = "Vdgraph" 

	version("2.2-7", md5="a631fe9101dfb3d36c54401de47290da")

