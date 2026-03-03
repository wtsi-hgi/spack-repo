# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecassorules(RPackage):
	"""Recursive Mining for Frequent Pattern and Confident Association
Rules

	Provides functions allowing the user to recursively extract frequent patterns and confident rules according to indicators of minimal support and minimal confidence. These functions are described in "Recursive Association Rule Mining" Abdelkader Mokkadem, Mariane Pelletier, Louis Raimbault (2020) <arXiv:2011.14195>.
	"""
	
	homepage = "https://github.com/LouisRaimbault/RecAssoRules-R"
	cran = "RecAssoRules" 

	version("1.0", md5="6bb9844a911aa9f5e92b0a96882d96a0")

	depends_on("r-rcpp", type=("build", "run"))
