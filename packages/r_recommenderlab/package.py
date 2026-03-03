# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecommenderlab(RPackage):
	"""Lab for Developing and Testing Recommender Algorithms

	Provides a research infrastructure to develop and evaluate
    collaborative filtering recommender algorithms. This includes a sparse 
    representation for user-item matrices, many popular algorithms, top-N recommendations,
    and cross-validation. Hahsler (2022) <doi:10.48550/arXiv.2205.12371>.
	"""
	
	homepage = "https://github.com/mhahsler/recommenderlab"
	cran = "recommenderlab" 

	version("1.0.6", md5="288f9309db3283ccecf29b9c5563a52d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-arules", type=("build", "run"))
	depends_on("r-proxy@0.4.26:", type=("build", "run"))
	depends_on("r-registry", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-recosystem", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
