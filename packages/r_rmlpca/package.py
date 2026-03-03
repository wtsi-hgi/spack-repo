# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmlpca(RPackage):
	"""Maximum Likelihood Principal Component Analysis

	R implementation of Maximum Likelihood Principal Component Analysis
    The main idea of this package is to have an alternative way of PCA for 
    subspace modeling that considers measurement errors.
    More details can be found in Peter D. Wentzell (2009) 
    <doi:10.1016/B978-0-444-64165-6.03029-9>.
	"""
	
	homepage = "https://github.com/renanestatcamp/RMLPCA"
	cran = "RMLPCA" 

	version("0.0.1", md5="b556a22c75fa87e512f345132560f72d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
