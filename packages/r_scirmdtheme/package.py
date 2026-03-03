# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScirmdtheme(RPackage):
	"""Upgraded 'Rmarkdown' Themes for Scientific Writing

	A set of 'Rmarkdown' themes for creating scientific and professional documents. Simple interface with features to ease navigation across the page and sub-pages.
	"""
	
	homepage = "https://github.com/oobianom/sciRmdTheme"
	cran = "sciRmdTheme" 

	version("0.1", md5="65b183ca107849a7e9e8cc0ace3a6a07")

	depends_on("r@3.4:", type=("build", "run"))
