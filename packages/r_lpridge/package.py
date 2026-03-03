# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpridge(RPackage):
	"""Local Polynomial (Ridge) Regression

	Local Polynomial Regression with Ridging.
	"""
	
	homepage = "https://curves-etc.r-forge.r-project.org/"
	cran = "lpridge" 

	version("1.1-0", md5="812202e4f5c6edf6cc6abf8a6c370f92")

