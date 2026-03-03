# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPm3(RPackage):
	"""Propensity Score Matching for Unordered 3-Group Data

	You can use this program for 3 sets of categorical data for propensity score matching.
            Assume that the data has 3 different categorical variables. You can use it to perform propensity matching of baseline indicator groupings. 
            The matching will make the differences in the baseline data smaller.
            This method was described by Alvaro Fuentes (2022) <doi:10.1080/00273171.2021.1925521>.
	"""
	
	cran = "pm3" 

	version("0.1.9", md5="3678c2a3ff471d615e368d5c89b242ec", url="https://cran.r-project.org/src/contrib/pm3_0.1.9.tar.gz")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-tableone", type=("build", "run"))
