# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKfpls(RPackage):
	"""Kernel Functional Partial Least Squares

	Implementation for kernel functional partial least squares (KFPLS) method. KFPLS method is developed for functional nonlinear models, and the method does not require strict constraints for the nonlinear structures. The crucial function of this package is KFPLS().
	"""
	
	cran = "KFPLS" 

	version("1.0", md5="c95f74672ee39bbd15d8d3c66ffef81e")

	depends_on("r-fda", type=("build", "run"))
