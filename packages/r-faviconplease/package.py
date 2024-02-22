# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFaviconplease(RPackage):
	"""Find the URL to the 'Favicon' for a Website

	Finds the URL to the 'favicon' for a website. This is useful if you
  want to display the 'favicon' in an HTML document or web application,
  especially if the website is behind a firewall.
	"""
	
	homepage = "https://github.com/jdblischak/faviconPlease"
	cran = "faviconPlease" 

	version("0.1.3", md5="f04359338e6d22d39fba5801d635fea6")

	depends_on("r-xml2", type=("build", "run"))
