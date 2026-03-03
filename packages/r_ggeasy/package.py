# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgeasy(RPackage):
	"""Easy Access to 'ggplot2' Commands

	Provides a series of aliases to commonly used but difficult 
    to remember 'ggplot2' sequences.
	"""
	
	homepage = "https://github.com/jonocarroll/ggeasy"
	cran = "ggeasy" 

	version("0.1.4", md5="63194d25f9fd56368ddf297b78fa2407")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
