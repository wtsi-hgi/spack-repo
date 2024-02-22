# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgroovy(RPackage):
	"""Groovy Language Integration

	Integrates the Groovy scripting language with the R Project for Statistical Computing.
	"""
	
	homepage = "http://groovy-lang.org/"
	cran = "rGroovy" 

	version("1.3", md5="9d7116a47aac3fa21bf30c2a96bfacee")

	depends_on("r-rjava", type=("build", "run"))
	depends_on("java@1.7:", type=("build", "link", "run"))
