# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDebif(RPackage):
	"""Bifurcation Analysis of Ordinary Differential Equation Systems

	Shiny application that performs bifurcation and phaseplane analysis of systems of ordinary 
    differential equations. The package allows for computation of equilibrium curves as a function of 
    a single free parameter, detection of transcritical, saddle-node and hopf bifurcation points along 
    these curves, and computation of curves representing these transcritical, saddle-node and hopf 
    bifurcation points as a function of two free parameters. The shiny-based GUI allows visualization 
    of the results in both 2D- and 3D-plots. The implemented methods for solution localisation and curve
    continuation are based on the book "Elements of applied bifurcation theory" (Kuznetsov, Y. A., 1995;
    ISBN: 0-387-94418-4).
	"""
	
	cran = "deBif" 

	version("0.1.8", md5="81152aa193bc3407e21030ae3648b043")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-desolve@1.3:", type=("build", "run"))
	depends_on("r-rootsolve@1.8:", type=("build", "run"))
	depends_on("r-rstudioapi@0.13:", type=("build", "run"))
	depends_on("r-shiny@1.7:", type=("build", "run"))
	depends_on("r-shinyjs@2.1:", type=("build", "run"))
	depends_on("r-shinydashboard@0.7:", type=("build", "run"))
	depends_on("r-shinydashboardplus@2:", type=("build", "run"))
