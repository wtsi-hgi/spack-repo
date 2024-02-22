# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaterfall(RPackage):
	"""Waterfall Charts

	Provides support for creating waterfall charts in R
    using both traditional base and lattice graphics.
	"""
	
	homepage = "https://jameshoward.us/software/waterfall/"
	cran = "waterfall" 

	version("1.0.2", md5="55dcf57382d84e6fcc6620de46a9c6c4")

	depends_on("r-lattice", type=("build", "run"))
