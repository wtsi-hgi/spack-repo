# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBpa(RPackage):
	"""Basic Pattern Analysis

	Run basic pattern analyses on character sets, digits, or combined
    input containing both characters and numeric digits. Useful for data
    cleaning and for identifying columns containing multiple or nonstandard
    formats.
	"""
	
	homepage = "https://github.com/bgreenwell/bpa"
	cran = "bpa" 

	version("0.1.1", md5="efbd111400d5e5cd9ecbd577c202f61e")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
