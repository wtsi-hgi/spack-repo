# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLatcontrol(RPackage):
	"""Evaluation of the Role of Control Variables in Structural
Equation Models

	Various opportunities to evaluate the effects of including one or more control variable(s) in structural equation models onto model-implied variances, covariances, and parameter estimates. The derivation of the methodology employed in this package can be obtained from Blötner (2023) <doi:10.31234/osf.io/dy79z>.
	"""
	
	cran = "latcontrol" 

	version("0.1.0", md5="51e88f51ce3618455cdb52b90e14c680")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
