# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSffdr(RPackage):
	"""Pleiotropy-informed significance analysis with functional false discovery rates"""
	
	homepage = "https://github.com/ajbass/sffdr"
	cran = "sffdr" 

	license("LGPL-2.0-or-later")

	version("1.1.0", sha256="3fcc5ac4f4caf44e9c5c8f297b6d378ec688fe5829a26f0d8ad612067a4662fe")
	version("1.0.0", sha256="1ff2627728b14a37fba8e7350701c66ee99964705f2a623ca1be567866e9567c")

	depends_on("r@4.1.0:")
	depends_on("r-ggplot2@3.5.1:")
	depends_on("r-patchwork@1.3.0:")
	depends_on("r-locfit")
	depends_on("r-qvalue")
	depends_on("r-fastglm")
	depends_on("r-withr")