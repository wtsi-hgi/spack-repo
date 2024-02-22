# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredictrace(RPackage):
	"""Predict the Race and Gender of a Given Name Using Census and
Social Security Administration Data

	Predicts the most common race of a surname and based on U.S. Census
    data, and the most common first named based on U.S. Social Security Administration data.
	"""
	
	homepage = "https://github.com/jacobkap/predictrace"
	cran = "predictrace" 

	version("2.0.1", md5="053c4295e7c500e5512d47fcea9557df")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
