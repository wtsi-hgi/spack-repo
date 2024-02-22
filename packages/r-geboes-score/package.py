# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeboesScore(RPackage):
	"""Evaluate the Geboes Score for Histology in Ulcerative Colitis

	Evaluate and validate the Geboes score for histological assessment
  of inflammation in ulcerative colitis.  The original Geboes score from Geboes,
  et al. (2000) <doi:10.1136/gut.47.3.404>, binary version from Li, et al.
  (2019) <doi:10.1093/ecco-jcc/jjz022>, and continuous version from Magro, et
  al. (2020) <doi:10.1093/ecco-jcc/jjz123> are all described and implemented.
	"""
	
	homepage = "https://billdenney.github.io/geboes.score/"
	cran = "geboes.score" 

	version("1.0.0", md5="a56b254b4cb6fb3e7a4e8b5da90ae4b4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
