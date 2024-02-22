# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcur(RPackage):
	"""Dimension Reduction with Dynamic CUR

	Dynamic CUR (dCUR) boosts the CUR decomposition (Mahoney MW., Drineas P. (2009) <doi:10.1073/pnas.0803205106>) varying the k, the number of columns and rows used, and its final purposes to help find the stage, which minimizes the relative error to reduce matrix dimension.
    The goal of CUR Decomposition is to give a better interpretation of the matrix decomposition employing proper variable selection in the data matrix, in a way that yields a simplified structure. Its origins come from analysis in genetics. 
    The goal of this package is to show an alternative to variable selection (columns) or individuals (rows). The idea proposed consists of adjusting the probability distributions to the leverage scores and selecting the best columns and rows that minimize the reconstruction error of the matrix approximation ||A-CUR||. It also includes a method that recalibrates the relative importance of the leverage scores according to an external variable of the user's interest.
	"""
	
	homepage = "https://www.cesargamboasanabria.com"
	cran = "dCUR" 

	version("1.0.1", md5="567941110646ff3d706c1fdcd77323b6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ppcor", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
