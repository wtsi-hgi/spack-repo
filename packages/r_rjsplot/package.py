# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRjsplot(RPackage):
	"""Interactive Graphs with R

	Creates interactive graphs with 'R'. It joins the data analysis power of R and the visualization libraries of JavaScript in one package.
	"""
	
	homepage = "https://rjsplot.usal.es"
	cran = "RJSplot" 

	version("2.7", md5="8ebff2e06f0423855a8bcd9d4097ba2e")

	depends_on("r@3:", type=("build", "run"))
