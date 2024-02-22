# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnsvplot(RPackage):
	"""National Road Safety Observatory (ONSV) Style for 'ggplot2'
Graphics

	Helps to create 'ggplot2' charts in the style used by the National 
    Road Safety Observatory (ONSV). The package includes functions to 
    customize 'ggplot2' objects with new theme and colors.
	"""
	
	homepage = "https://github.com/pabsantos/onsvplot/"
	cran = "onsvplot" 

	version("0.3.2", md5="b7a429d94a7e55907eba47ef16e800f6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
