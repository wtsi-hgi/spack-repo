# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRadarboxplot(RPackage):
	"""Implementation of the Radar-Boxplot

	Creates the radar-boxplot, a plot that was created by the 
    author during his Ph.D. in forest resources. 
    The radar-boxplot is a visualization feature suited for  
    multivariate classification/clustering. It provides an intuitive 
    deep understanding of the data.
	"""
	
	homepage = "https://github.com/caiohamamura/radarBoxplot-R"
	cran = "radarBoxplot" 

	version("1.0.5", md5="98a2479160015498ecb45be83ad22dd4")

	depends_on("r@3.5:", type=("build", "run"))
