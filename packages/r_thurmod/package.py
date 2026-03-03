# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThurmod(RPackage):
	"""Thurstonian CFA and Thurstonian IRT Modeling

	Fit Thurstonian forced-choice models (CFA (simple and factor) and IRT) in R. This package allows for the analysis of item response modeling (IRT) as well as confirmatory factor analysis (CFA) in the Thurstonian framework. Currently, estimation can be performed by 'Mplus' and 'lavaan'. References:
  Brown & Maydeu-Olivares (2011) <doi:10.1177/0013164410375112>;
  Jansen, M. T., & Schulze, R. (in review). The Thurstonian linked block design: Improving Thurstonian modeling for paired comparison and ranking data.;
  Maydeu-Olivares & Böckenholt (2005) <doi:10.1037/1082-989X.10.3.285>.
	"""
	
	homepage = "https://github.com/MarkusTJansen/ThurMod"
	cran = "ThurMod" 

	version("1.1.11", md5="338899a8e0d676b2fa474f679827c1d4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
