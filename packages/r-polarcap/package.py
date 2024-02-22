# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolarcap(RPackage):
	"""Access the Polarization in Comparative Attitudes Project

	Distributes data from the Polarization in Comparative Attitudes Project. Helper
    functions enable data retrieval in wide and tidy formats for user-defined
    countries and years. Provides support for case-insensitive country names in many
    languages. Mehlhaff (2022) <https://imehlhaff.net/files/Polarization%20and%20Democracy.pdf>.
	"""
	
	homepage = "https://github.com/imehlhaff/PolarCAP"
	cran = "PolarCAP" 

	version("1.0.1", md5="1b0378c7648e4084de6cee05d92b4b31")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-countrycode", type=("build", "run"))
