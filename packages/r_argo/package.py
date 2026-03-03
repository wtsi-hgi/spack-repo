# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArgo(RPackage):
	"""Accurate Estimation of Influenza Epidemics using Google Search
Data

	Augmented Regression with General Online data (ARGO) for accurate estimation of influenza epidemics in United States on national level, regional level and state level. It replicates the method introduced in paper Yang, S., Santillana, M. and Kou, S.C. (2015) <doi:10.1073/pnas.1515373112>; Ning, S., Yang, S. and Kou, S.C. (2019) <doi:10.1038/s41598-019-41559-6>; Yang, S., Ning, S. and Kou, S.C. (2021) <doi:10.1038/s41598-021-83084-5>.
	"""
	
	cran = "argo" 

	version("3.0.2", md5="6a97c5c0c0c9e624b6ef6671d6c53bef")

	depends_on("r-xts", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
