# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvquickgraphs(RPackage):
	"""Quick Multivariate Graphs

	Functions used for graphing in multivariate contexts. These 
    functions are designed to support produce reasonable graphs with minimal 
    input of graphing parameters. The motivation for these functions was to 
    support students learning multivariate concepts and R - there may be 
    other functions and packages better-suited to practical data analysis. For
    details about the ellipse methods see Johnson and Wichern (2007, 
    ISBN:9780131877153).
	"""
	
	cran = "MVQuickGraphs" 

	version("0.1.2", md5="803ccd64dad522b060a7eca74b7b7f89")

	depends_on("r-plotrix", type=("build", "run"))
