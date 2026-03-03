# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTelegram(RPackage):
	"""R Wrapper Around the Telegram Bot API

	R wrapper around the Telegram Bot API (http://core.telegram.org/bots/api) to access Telegram's messaging facilities with ease (e.g. you send messages, images, files from R to your smartphone).
	"""
	
	homepage = "http://github.com/lbraglia/telegram"
	cran = "telegram" 

	version("0.6.0", md5="a6bb6c13df760fd02935877f4a8c19b3")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
