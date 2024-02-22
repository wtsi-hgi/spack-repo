# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMisscp(RPackage):
	"""Change Point Detection with Missing Values

	A four step change point detection method that can detect break points with the presence of missing values proposed by Liu and Safikhani (2023) <https://drive.google.com/file/d/1a8sV3RJ8VofLWikTDTQ7W4XJ76cEj4Fg/view?usp=drive_link>.
	"""
	
	cran = "MissCP" 

	version("0.1.0", md5="c408823bc25d42251be338958b5e125e")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-sparsevar", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
