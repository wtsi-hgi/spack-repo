# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKelvin(RPackage):
	"""Calculate Solutions to the Kelvin Differential Equation using
Bessel Functions

	Uses Bessel functions to calculate the
    fundamental and complementary analytic solutions to the
    Kelvin differential equation.
	"""
	
	homepage = "https://github.com/abarbour/kelvin"
	cran = "kelvin" 

	version("2.0-2", md5="3d83eb7d6481e8873af475985846159d")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-bessel@0.5.4:", type=("build", "run"))
