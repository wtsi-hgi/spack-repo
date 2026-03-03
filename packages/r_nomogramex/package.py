# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNomogramex(RPackage):
	"""Extract Equations from a Nomogram

	
  A nomogram can not be easily applied,
    because it is difficult to calculate the points or even the survival probability.
  The package, including a function of nomogramEx(),
    is to extract the polynomial equations to calculate the points of each variable,
    and the survival probability corresponding to the total points.
	"""
	
	cran = "nomogramEx" 

	version("3.0", md5="def4fc8212c9e680c69c0bce6d848d71")

	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
