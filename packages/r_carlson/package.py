# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCarlson(RPackage):
	"""Carlson Elliptic Integrals and Incomplete Elliptic Integrals

	Evaluation of the Carlson elliptic integrals and the
    incomplete elliptic integrals with complex arguments. The
    implementations use Carlson's algorithms <doi:10.1007/BF02198293>.
    Applications of elliptic integrals include probability distributions,
    geometry, physics, mechanics, electrodynamics, statistical mechanics,
    astronomy, geodesy, geodesics on conics, and magnetic field
    calculations.
	"""
	
	homepage = "https://github.com/stla/Carlson"
	cran = "Carlson" 

	version("3.0.0", md5="6e587c6e09dbd8678831e2712a537aea")

	depends_on("r-rcpp", type=("build", "run"))
