# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInstar(RPackage):
	"""Access to Instagram API via R

	Provides an interface to the Instagram API <https://instagram.com/
    developer/>, which allows R users to download public pictures filtered by
    hashtag, popularity, user or location, and to access public users' profile data.
	"""
	
	homepage = "https://github.com/pablobarbera/instaR"
	cran = "instaR" 

	version("0.2.4", md5="e22a8637dd9f7beba388b56783859cb5")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
