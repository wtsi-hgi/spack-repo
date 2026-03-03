# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrekcolors(RPackage):
	"""Star Trek Color Palettes

	Provides a dataset of predefined color palettes based on the Star Trek science fiction series, associated color palette functions, 
    and additional functions for generating customized palettes that are on theme. The package also offers functions for applying 
    the palettes to plots made using the 'ggplot2' package.
	"""
	
	homepage = "https://github.com/leonawicz/trekcolors"
	cran = "trekcolors" 

	version("0.1.3", md5="9db9d6e89150aabdd2972ead4d633309")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
