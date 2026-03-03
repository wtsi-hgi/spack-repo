# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnelogin(RPackage):
	"""Interact with the 'OneLogin' API

	The identity provider ['OneLogin']<http://onelogin.com> is used for 
  authentication via Single Sign On (SSO). This package provides an R interface to their API.
	"""
	
	cran = "onelogin" 

	version("0.2.0", md5="7c88f1d74588b710a73290bdf871bcce")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-safer", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
