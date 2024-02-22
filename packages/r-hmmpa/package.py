# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmmpa(RPackage):
	"""Analysing Accelerometer Data Using Hidden Markov Models

	Analysing time-series accelerometer data to quantify length and 
             intensity of physical activity using hidden Markov models. 
             It also contains the traditional cut-off point method.
             Witowski V, Foraita R, Pitsiladis Y, Pigeot I, 
             Wirsik N (2014)<doi:10.1371/journal.pone.0114089>.
	"""
	
	cran = "HMMpa" 

	version("1.0.1", md5="04c563c85de65c0c63f1f4320f2d530a")

	depends_on("r@2.10:", type=("build", "run"))
