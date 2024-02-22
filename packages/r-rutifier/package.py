# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRutifier(RPackage):
	"""Chilean Rol Unico Tributario

	A RUT (Rol Unico Tributario) is an unique and personal identification number implemented in Chile to identify citizens and taxpayers. Rutifier allows to validate if a RUT exist or not and change between the different formats a RUT can have.
	"""
	
	cran = "rutifier" 

	version("1.0.4", md5="08ba06c28b1260ef9ea753e3cd894dad")

	depends_on("r-r-utils", type=("build", "run"))
