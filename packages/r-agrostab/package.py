# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgrostab(RPackage):
	"""Stability Analysis for Agricultural Research

	Statistical procedures to perform stability analysis in plant breeding and to identify stable genotypes under diverse environments. It is possible to calculate coefficient of homeostaticity by Khangildin et al. (1979), variance of specific adaptive ability by Kilchevsky&Khotyleva (1989), weighted homeostaticity index by Martynov (1990), steadiness of stability index by Udachin (1990), superiority measure by Lin&Binn (1988) <doi:10.4141/cjps88-018>, regression on environmental index by Erberhart&Rassel (1966) <doi:10.2135/cropsci1966.0011183X000600010011x>, Tai's (1971) stability parameters <doi:10.2135/cropsci1971.0011183X001100020006x>, stability variance by Shukla (1972) <doi:10.1038/hdy.1972.87>, ecovalence by Wricke (1962), nonparametric stability parameters by Nassar&Huehn (1987) <doi:10.2307/2531947>, Francis&Kannenberg's parameters of stability (1978) <doi:10.4141/cjps78-157>.
	"""
	
	cran = "agrostab" 

	version("0.1.0", md5="6f2234f56e281cd1475d048522cadb11")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
