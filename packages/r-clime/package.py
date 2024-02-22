# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClime(RPackage):
	"""Constrained L1-Minimization for Inverse (Covariance) Matrix
Estimation

	A robust constrained L1 minimization method for estimating a large sparse inverse covariance matrix (aka precision matrix), and recovering its support for building graphical models.  The computation uses linear programming.  The method was published in TT Cai, W Liu, X Luo (2011) <doi:10.1198/jasa.2011.tm10155>.
	"""
	
	cran = "clime" 

	version("0.5.0", md5="240ec5600484bdaccfff48866fc13ec1")

	depends_on("r-lpsolve", type=("build", "run"))
