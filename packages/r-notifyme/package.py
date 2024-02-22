# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNotifyme(RPackage):
	"""Send Alerts to your Cellphone and Phillips Hue Lights

	Functions to flash your hue lights, or text yourself, from R. Designed to be used with long running scripts.
	"""
	
	homepage = "https://github.com/epijim/notifyme"
	cran = "notifyme" 

	version("0.3.0", md5="09f60d37dc374b1442c4ff6a2106b3c6")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
