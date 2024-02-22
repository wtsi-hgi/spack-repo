# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsocodes(RPackage):
	"""Selected ISO Codes

	ISO language, territory, currency, script and character codes.
  Provides ISO 639 language codes, ISO 3166 territory codes, ISO 4217
  currency codes, ISO 15924 script codes, and the ISO 8859 character codes
  as well as the UN M.49 area codes.
	"""
	
	cran = "ISOcodes" 

	version("2024.02.12", md5="65379246fbe90371859da3d4df8b8ad0")

	depends_on("r@3.5:", type=("build", "run"))
