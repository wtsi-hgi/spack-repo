# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSearchconsoler(RPackage):
	"""Google Search Console R Client

	Provides an interface with the Google Search Console,
    formally called Google Webmaster Tools.
	"""
	
	homepage = "http://code.markedmondson.me/searchConsoleR/"
	cran = "searchConsoleR" 

	version("0.4.0", md5="b3c1b983706854bc5883f27150db4003")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-googleauthr@1:", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
