# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResi(RPackage):
	"""Robust Effect Size Index (RESI) Estimation

	Summarize model output using a robust effect size index. The index is introduced in Vandekar, Tao, & Blume (2020) <doi:10.1007/s11336-020-09698-2>.
	"""
	
	homepage = "https://statimagcoll.github.io/RESI/"
	cran = "RESI" 

	version("1.2.4", md5="16d9edbfebffeed838ddaf34b4834a21")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-aod", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-clubsandwich", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
