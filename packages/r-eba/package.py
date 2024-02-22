# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REba(RPackage):
	"""Elimination-by-Aspects Models

	Fitting and testing multi-attribute probabilistic choice
  models, especially the Bradley-Terry-Luce (BTL) model (Bradley &
  Terry, 1952 <doi:10.1093/biomet/39.3-4.324>; Luce, 1959),
  elimination-by-aspects (EBA) models (Tversky, 1972 <doi:10.1037/h0032955>),
  and preference tree (Pretree) models (Tversky & Sattath, 1979
  <doi:10.1037/0033-295X.86.6.542>).
	"""
	
	homepage = "http://www.mathpsy.uni-tuebingen.de/wickelmaier"
	cran = "eba" 

	version("1.10-0", md5="8a8c1c03e417932c997c787e667531ed")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-psychotools", type=("build", "run"))
