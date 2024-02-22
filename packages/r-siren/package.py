# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSiren(RPackage):
	"""Hybrid FA-CFA for Controlling Acquiescence in Restricted
Factorial Solutions

	Performs hybrid multi-stage factor analytic procedure for controlling acquiescence in restricted solutions (Ferrando & Lorenzo-Seva, 2000 <https://www.uv.es/revispsi/articulos3.00/ferran7.pdf>).
	"""
	
	cran = "siren" 

	version("1.0.4", md5="f530fc6f72c33113281dce762cc29b63")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-efa-mrfa", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
