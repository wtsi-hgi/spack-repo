# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExposition(RPackage):
	"""Exploratory Analysis with the Singular Value Decomposition

	A variety of descriptive multivariate analyses with the singular value decomposition,
    such as principal components analysis, correspondence analysis, and multidimensional scaling.
    See An ExPosition of the Singular Value Decomposition in R (Beaton et al 2014) <doi:10.1016/j.csda.2013.11.006>.
	"""
	
	cran = "ExPosition" 

	version("2.8.23", md5="7864f3dcb5f54b1b51230b648dbc281b")

	depends_on("r-prettygraphs@2.1.4:", type=("build", "run"))
