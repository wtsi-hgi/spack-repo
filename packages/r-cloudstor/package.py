# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCloudstor(RPackage):
	"""Simplifies Access to Cloudstor API

	Access Cloudstor via their WebDAV API. This package can read, write, and navigate Cloudstor from R.
	"""
	
	homepage = "https://pdparker.github.io/cloudstoR/"
	cran = "cloudstoR" 

	version("0.2.0", md5="263acfaf402502715d8cd8865d56e97e")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
