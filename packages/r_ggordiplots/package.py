# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgordiplots(RPackage):
	"""Make 'ggplot2' Versions of Vegan's Ordiplots

	The 'vegan' package includes several functions for adding features
  to ordination plots: ordiarrows(),  ordiellipse(), ordihull(),
  ordispider() and ordisurf(). This package adds these same   features to 
  ordination plots made with 'ggplot2'. In addition, gg_ordibubble() sizes
  points relative to the value of an environmental variable. 
	"""
	
	homepage = "https://github.com/jfq3/ggordiplots"
	cran = "ggordiplots" 

	version("0.4.3", md5="7db045025c5a969effd66c8250548231")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-vegan@2.5.2:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
