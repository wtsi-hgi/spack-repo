# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXergmCommon(RPackage):
	"""Common Infrastructure for Extensions of Exponential Random Graph
Models

	Datasets and definitions of generic functions used in dependencies of the 'xergm' package.
	"""
	
	homepage = "http://github.com/leifeld/xergm.common"
	cran = "xergm.common" 

	version("1.7.8", md5="c04cb07bfa5a1d332220c58d58394729")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-ergm@3.5.1:", type=("build", "run"))
	depends_on("r-network@1.13:", type=("build", "run"))
