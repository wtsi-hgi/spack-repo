# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrouptesting(RPackage):
	"""Simulating and Modeling Group (Pooled) Testing Data

	Provides an expectation-maximization (EM) algorithm using the approach introduced in Warasi (2021) <doi:10.1080/03610918.2021.2009867>. The EM algorithm can be used to estimate the prevalence (overall proportion) of a disease and to estimate a binary regression model from among the class of generalized linear models based on group testing data. The estimation framework we consider offers a flexible and general approach; i.e., its application is not limited to any specific group testing protocol. Consequently, the EM algorithm can model data arising from simple pooling as well as advanced pooling such as hierarchical testing, array testing, and quality control pooling. Also, provided are functions that can be used to conduct the Wald tests described in Buse (1982) <doi:10.1080/00031305.1982.10482817> and to simulate the group testing data described in Kim et al. (2007) <doi:10.1111/j.1541-0420.2007.00817.x>.
	"""
	
	cran = "groupTesting" 

	version("1.1.0", md5="533733963d481b5c9079ec345ad41602")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
