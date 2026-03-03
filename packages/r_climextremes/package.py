# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClimextremes(RPackage):
	"""Tools for Analyzing Climate Extremes

	Functions for fitting GEV and POT (via point process fitting)
    models for extremes in climate data, providing return values, return
    probabilities, and return periods for stationary and nonstationary models.
    Also provides differences in return values and differences in log return
    probabilities for contrasts of covariate values. Functions for estimating risk
    ratios for event attribution analyses, including uncertainty. Under the hood,
    many of the functions use functions from 'extRemes', including for fitting the
    statistical models. Details are given in Paciorek, Stone, and Wehner (2018)
    <doi:10.1016/j.wace.2018.01.002>.
	"""
	
	homepage = "https://bitbucket.org/lbl-cascade/climextremes-dev"
	cran = "climextRemes" 

	version("0.3.1", md5="a614b3a56e041e761ede2a5f46485c72")

	depends_on("r-extremes@2:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
