# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgghost(RPackage):
	"""Capture the Spirit of Your 'ggplot2' Calls

	Creates a reproducible 'ggplot2' object by storing the data and calls. 
	"""
	
	homepage = "https://github.com/jonocarroll/ggghost"
	cran = "ggghost" 

	version("0.2.1", md5="bc26b955e21283af89bdf41f0c5158e2")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-animation", type=("build", "run"))
