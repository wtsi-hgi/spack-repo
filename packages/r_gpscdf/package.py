# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpscdf(RPackage):
	"""Generalized Propensity Score Cumulative Distribution Function

	Implements the generalized propensity score cumulative distribution
    function proposed by Greene (2017)
    <https://digitalcommons.library.tmc.edu/dissertations/AAI10681743/>.
    A single scalar balancing score is calculated for any generalized propensity
    score vector with three or more treatments. This balancing score is used for
    propensity score matching and stratification in outcome analyses when analyzing
    either ordinal or multinomial treatments.
	"""
	
	cran = "GPSCDF" 

	version("0.1.1", md5="c0b5ec9ea7dd8a52f908d0cf67ec67ce")

	depends_on("r-dplyr@0.7.6:", type=("build", "run"))
	depends_on("r-nbpmatching@1.5.1:", type=("build", "run"))
	depends_on("r-nnet@7.3.12:", type=("build", "run"))
	depends_on("r-mass@7.3.49:", type=("build", "run"))
	depends_on("r-survival@2.41.3:", type=("build", "run"))
