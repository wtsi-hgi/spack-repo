# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGnomonicm(RPackage):
	"""Estimate Natural Mortality for Different Life Stages

	Estimate natural mortality (M) throughout the life history for organisms, mainly fish and invertebrates, based on gnomonic interval approach proposed by Caddy (1996) <doi:10.1051/alr:1996023> and Martinez-Aguilar et al. (2005) <doi:10.1016/j.fishres.2004.04.008>.
    It includes estimation of duration of each gnomonic interval (life stage), the constant probability of death (G), and some basic plots.
	"""
	
	cran = "gnomonicM" 

	version("1.0.1", md5="941ee028d77859079392229c066fa2a5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-triangle", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
