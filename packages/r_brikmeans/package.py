# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrikmeans(RPackage):
	"""Package for Brik, Fabrik and Fdebrik Algorithms to Initialise
Kmeans

	Implementation of the BRIk, FABRIk and FDEBRIk algorithms 
        to initialise k-means. These methods are intended for the 
        clustering of multivariate and functional data, respectively.
        They make use of the Modified Band Depth and bootstrap to 
        identify appropriate initial seeds for k-means, which are 
        proven to be better options than many techniques in the 
        literature. Torrente and Romo (2021) <doi:10.1007/s00357-020-09372-3>
        It makes use of the functions kma and kma.similarity, from the 
        archived package fdakma, by Alice Parodi et al.
	"""
	
	cran = "briKmeans" 

	version("1.0", md5="99027087228eb0ff73caa4fcea7fa216")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-depthtools", type=("build", "run"))
	depends_on("r-splines2", type=("build", "run"))
