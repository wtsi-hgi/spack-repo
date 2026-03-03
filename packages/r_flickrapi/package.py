# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlickrapi(RPackage):
	"""Access to Flickr API

	Provides an interface to the Flickr API <https://www.flickr.com/services/api/>
      and allows R users to download data on Flickr.
	"""
	
	cran = "FlickrAPI" 

	version("0.1.0.1", md5="91ac53dc8ccda42d8db02faf2fd47db4")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
