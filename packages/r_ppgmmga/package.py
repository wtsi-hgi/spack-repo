# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpgmmga(RPackage):
	"""Projection Pursuit Based on Gaussian Mixtures and Evolutionary
Algorithms

	Projection Pursuit (PP) algorithm for dimension reduction based on Gaussian Mixture Models (GMMs) for density estimation using Genetic Algorithms (GAs) to maximise an approximated negentropy index. For more details see Scrucca and Serafini (2019) <doi:10.1080/10618600.2019.1598871>.
	"""
	
	homepage = "https://github.com/luca-scr/ppgmmga"
	cran = "ppgmmga" 

	version("1.3", md5="64466f57df2e7681d74e141898c008c8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mclust@5.4:", type=("build", "run"))
	depends_on("r-ga@3.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7:", type=("build", "run"))
