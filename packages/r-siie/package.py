# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSiie(RPackage):
	"""Superior Identification Index and Its Extensions

	Calculate superior identification index and its extensions.
    Measure the performance of journals based on how well they could 
    identify the top papers by any index (e.g. citation indices) according to Huang & Yang. 
    (2022) <doi:10.1007/s11192-022-04372-z>. These methods could be extended to 
    evaluate other entities such as institutes, countries, etc.
	"""
	
	cran = "siie" 

	version("0.4.0", md5="cb4dfcb91d9f9873d2ece1dab489358f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
