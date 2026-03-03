# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovidmutations(RPackage):
	"""Mutation Analysis Toolkit for COVID-19 (Coronavirus Disease
2019)

	A feasible framework for mutation analysis and reverse transcription 
  polymerase chain reaction (RT-PCR) assay evaluation of COVID-19, including 
  mutation profile visualization, statistics and mutation ratio of each assay. 
  The mutation ratio is conducive to evaluating the coverage of RT-PCR assays in 
  large-sized samples. Mercatelli, D. and Giorgi, F. M. (2020) 
  <doi:10.20944/preprints202004.0529.v1>.
	"""
	
	homepage = "https://github.com/MSQ-123/CovidMutations"
	cran = "CovidMutations" 

	version("0.1.3", md5="e2472882cd5d6253e15d37f62e47dc62")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
