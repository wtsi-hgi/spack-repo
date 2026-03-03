# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLearnpca(RPackage):
	"""Functions, Data Sets and Vignettes to Aid in Learning Principal
Components Analysis (PCA)

	Principal component analysis (PCA) is one of the most widely used data analysis techniques.  This package provides a series of vignettes explaining PCA starting from basic concepts. The primary purpose is to serve as a self-study resource for anyone wishing to understand PCA better. A few convenience functions are provided as well.
	"""
	
	homepage = "https://bryanhanson.github.io/LearnPCA/"
	cran = "LearnPCA" 

	version("0.2.0", md5="d204c8890303787e66b69c280058f898")

	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
