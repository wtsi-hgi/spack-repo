# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJsonnormalize(RPackage):
	"""Normalization of 'JSON' Strings

	Provides a function allowing to normalize a 'JSON' string,
    for example by adding double quotes around the keys when they are
    missing. Also provides 'RStudio' addins for the same purpose.
	"""
	
	homepage = "https://github.com/stla/jsonNormalize"
	cran = "jsonNormalize" 

	version("1.0.0", md5="3d05df2344ed05b47cd220e80cbe4aeb")

	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
