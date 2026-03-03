# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptsig(RPackage):
	"""Optimal Level of Significance for Regression and Other
Statistical Tests

	The optimal level of significance is calculated based on a decision-theoretic approach. The optimal level is chosen so that the expected loss from hypothesis testing is minimized. A range of statistical tests are covered, including the test for the population mean, population proportion, and a linear restriction in a multiple regression model. 
             The details are covered in Kim and Choi (2020) <doi:10.1111/abac.12172>, and Kim (2021) <doi:10.1080/00031305.2020.1750484>. 
	"""
	
	cran = "OptSig" 

	version("2.2", md5="074baf87ead732f5f6d330e0e292d319")

	depends_on("r-pwr", type=("build", "run"))
