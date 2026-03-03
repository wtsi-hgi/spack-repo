# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRode(RPackage):
	"""Ordinary Differential Equation (ODE) Solvers Written in R Using
S4 Classes

	Show physics, math and engineering students how an ODE solver
    is made and how effective R classes can be for the construction of
    the equations that describe natural phenomena. Inspiration for this work 
    comes from the book on "Computer Simulations in Physics" 
    by Harvey Gould, Jan Tobochnik, and Wolfgang Christian. 
    Book link: <http://www.compadre.org/osp/items/detail.cfm?ID=7375>.
	"""
	
	homepage = "https://github.com/f0nzie/rODE"
	cran = "rODE" 

	version("0.99.6", md5="3ecfe52854b52b89d062ac8e1bdf394e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
