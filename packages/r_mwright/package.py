# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMwright(RPackage):
	"""Mainardi-Wright Family of Distributions

	Implements random  number generation, plotting, and estimation algorithms for the two-parameter one-sided and two-sided M-Wright (Mainardi-Wright) family.
             The M-Wright  distributions naturally generalize the widely used one-sided (Airy and half-normal or half-Gaussian) and symmetric (Airy and Gaussian or normal) models. 
             These are widely studied in time-fractional differential equations. References: Cahoy and Minkabo (2017) <doi:10.3233/MAS-170388>; Cahoy (2012) <doi:10.1007/s00180-011-0269-x>; Cahoy (2012) <doi:10.1080/03610926.2010.543299>; Cahoy (2011); Mainardi, Mura, and Pagnini (2010) <doi:10.1155/2010/104505>.
	"""
	
	cran = "MWright" 

	version("0.3.2", md5="b5669c818f63ff9fc0193096d563ab5e")

	depends_on("r-cubature", type=("build", "run"))
