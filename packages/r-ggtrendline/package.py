# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgtrendline(RPackage):
	"""Add Trendline and Confidence Interval to 'ggplot'

	Add trendline and confidence interval of linear or nonlinear regression model and
    show equation to 'ggplot' as simple as possible. For a general overview of the methods used in
	  this package, see Ritz and Streibig (2008) <doi:10.1007/978-0-387-09616-2> and 
	  Greenwell and Schubert Kabban (2014) <doi:10.32614/RJ-2014-009>.
	"""
	
	homepage = "https://github.com/PhDMeiwp/ggtrendline"
	cran = "ggtrendline" 

	version("1.0.3", md5="97d24214b36da1a2beaf0e079512c650")

	depends_on("r@3.5.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
