# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgrf(RPackage):
	"""International Geomagnetic Reference Field

	The 13th generation International Geomagnetic Reference Field (IGRF).
 A standard spherical harmonic representation of the Earth's main field.
	"""
	
	homepage = "https://github.com/bluegreen-labs/igrf"
	cran = "igrf" 

	version("1.0", md5="ee5fdd39be7dead73086e7e4c3096c0f")

	depends_on("r@3.6:", type=("build", "run"))
