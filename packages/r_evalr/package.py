# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvalr(RPackage):
	"""Evaluation of Unverified Code

	The purpose of this package is to generate trees and validate unverified code. Trees are made by parsing a statement into a verification tree data structure. This will make it easy to port the statement into another language. Safe statement evaluations are done by executing the verification trees.
	"""
	
	cran = "evalR" 

	version("0.0.1", md5="aa139efb67b8290d256ec87b0582ab8d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
