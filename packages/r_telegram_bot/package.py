# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTelegramBot(RPackage):
	"""Develop a 'Telegram Bot' with R

	Provides a pure interface for the 'Telegram Bot API'
    <http://core.telegram.org/bots/api>. In addition to the pure API
    implementation, it features a number of tools to make the development of
    'Telegram' bots with R easy and straightforward, providing an easy-to-use
    interface that takes some work off the programmer.
	"""
	
	homepage = "https://github.com/ebeneditos/telegram.bot"
	cran = "telegram.bot" 

	version("3.0.0", md5="fc4e196018649c3d81ff38e4131eccc0")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
