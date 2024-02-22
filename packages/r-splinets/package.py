# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplinets(RPackage):
	"""Functional Data Analysis using Splines and Orthogonal Spline
Bases

	Splines are efficiently represented through their Taylor expansion at the knots. The representation accounts for the support sets and is thus suitable for sparse functional data. Two cases of boundary conditions are considered: zero-boundary or periodic-boundary for all derivatives except the last. The periodical splines are represented graphically using polar coordinates. The B-splines and orthogonal bases of splines that reside on small total support are implemented. The orthogonal bases are referred to as 'splinets' and are utilized for functional data analysis. Random spline generator is implemented as well as  all fundamental algebraic and calculus operations on splines.  The optimal, in the least square sense, functional fit by 'splinets' to data consisting of sampled values of functions as well as splines build over another set of knots is obtained and used for functional data analysis.  <arXiv:2102.00733>, <doi:10.1016/j.cam.2022.114444>,  <arXiv:2302.07552>. 
	"""
	
	cran = "Splinets" 

	version("1.5.0", md5="0afa2e601cb7da7aa0188ab604aee252")

	depends_on("r@3.5:", type=("build", "run"))
