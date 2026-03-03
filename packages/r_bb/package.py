# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBb(RPackage):
	"""Solving and Optimizing Large-Scale Nonlinear Systems

	Barzilai-Borwein spectral methods for solving nonlinear
        system of equations, and for optimizing nonlinear objective
        functions subject to simple constraints. A tutorial style
        introduction to this package is available in a vignette on the
        CRAN download page or, when the package is loaded in an R
        session, with vignette("BB").
	"""
	
	homepage = "http://www.jhsph.edu/agingandhealth/People/Faculty_personal_pages/Varadhan.html"
	cran = "BB" 

	version("2019.10-1", md5="34607566d639cb346e1b979767945fef")

	depends_on("r@2.6.1:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
