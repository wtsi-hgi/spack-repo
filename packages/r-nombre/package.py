# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNombre(RPackage):
	"""Number Names

	Converts numeric vectors to character vectors of English
    number names. Provides conversion to cardinals, ordinals, numerators,
    and denominators. Supports negative and non-integer numbers.
	"""
	
	homepage = "https://nombre.rossellhayes.com"
	cran = "nombre" 

	version("0.4.1", md5="00043944b31852920acc2335cf8770e3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fracture@0.2.1:", type=("build", "run"))
