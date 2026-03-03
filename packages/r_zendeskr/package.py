# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZendeskr(RPackage):
	"""Zendesk API Wrapper

	This package provides an R wrapper for the Zendesk API
	"""
	
	cran = "zendeskR" 

	version("0.4", md5="9cf1fb871a0b23b8b987853dcda1fc69")

	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
