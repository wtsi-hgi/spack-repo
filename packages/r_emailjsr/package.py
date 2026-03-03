# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmailjsr(RPackage):
	"""'emailjs' Support

	Use 'emailjs' API easily in 'R'. This package is not official. <https://www.emailjs.com/docs/rest-api/send/>. You can send e-mail with 'emailjs' with function, based on 'httr'. You can also make a 'shiny' ui and server function. It can be used for making feedback form, inquiry, and so on.
	"""
	
	cran = "emailjsr" 

	version("0.0.2", md5="1828ee64472eec938a3d1a0b4897fd66")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shiny-i18n", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-shinybrowser", type=("build", "run"))
