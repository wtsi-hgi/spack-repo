# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredfairness(RPackage):
	"""Discrimination Mitigation for Machine Learning Models

	Based on different statistical definitions of discrimination, several methods have been proposed to detect and mitigate social inequality in machine learning models. 
  This package aims to provide an alternative to fairness treatment in predictive models. The ROC method implemented in this package
  is described by Kamiran, Karim and Zhang (2012) <https://ieeexplore.ieee.org/document/6413831/>.
	"""
	
	cran = "predfairness" 

	version("0.1.0", md5="2f064ff39d509c4112ee17558881154d")

	depends_on("r@3.5:", type=("build", "run"))
