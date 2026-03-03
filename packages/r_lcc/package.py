# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLcc(RPackage):
	"""Longitudinal Concordance Correlation

	Estimates the longitudinal concordance correlation to access the longitudinal agreement profile. The estimation approach implemented is variance components approach based on polynomial mixed effects regression model, as proposed by Oliveira, Hinde and Zocchi (2018) <doi:10.1007/s13253-018-0321-1>.  In addition, non-parametric confidence intervals were implemented using percentile method or normal-approximation based on Fisher Z-transformation.
	"""
	
	cran = "lcc" 

	version("1.1.4", md5="4c4e8f3f0dad17e7191c7a5a8bfe16cc")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-nlme@3.1.124:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-hnp", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
