# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMod(RPackage):
	"""Lightweight and Self-Contained Modules for Code Organization

	Creates modules inline or from a file. Modules can contain any R object and be nested. Each module have their own scope and package "search path" that does not interfere with one another or the user's working environment.
	"""
	
	homepage = "https://github.com/iqis/mod"
	cran = "mod" 

	version("0.1.3", md5="32e70f1080f48a205c56d23d43b66608")

