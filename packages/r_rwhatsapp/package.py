# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwhatsapp(RPackage):
	"""Import and Handling for 'WhatsApp' Chat Logs

	A straightforward, easy-to-use and robust parsing package which aims to
    digest history files from the popular messenger service 'WhatsApp' in all locales
    and from all devices.
	"""
	
	homepage = "https://github.com/JBGruber/rwhatsapp"
	cran = "rwhatsapp" 

	version("0.2.4", md5="76939a961ab6d7c2871c89896c89f51f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringi@1.1.7:", type=("build", "run"))
	depends_on("r-tibble@1.4:", type=("build", "run"))
