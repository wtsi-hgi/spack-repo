# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSupportBws3(RPackage):
	"""Tools for Case 3 Best-Worst Scaling

	Provides basic functions that support an implementation of multi-profile case (Case 3) best-worst scaling (BWS). Case 3 BWS is a question-based survey method to elicit people's preferences for attribute levels. Case 3 BWS constructs various combinations of attribute levels (profiles) and then asks respondents to select the best and worst profiles in each choice set. A main function creates a dataset for the analysis from the choice sets and the responses to the questions. For details on Case 3 BWS, refer to Louviere et al. (2015) <doi:10.1017/CBO9781107337855>.
	"""
	
	cran = "support.BWS3" 

	version("0.2-1", md5="b9d52c993e44fa2531d08ed212402742", url="https://cran.r-project.org/src/contrib/support.BWS3_0.2-1.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
