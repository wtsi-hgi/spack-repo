# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCooccurrenceaffinity(RPackage):
	"""Affinity in Co-Occurrence Data

	Computes a novel metric of affinity between two entities based on their co-occurrence 
  (using binary presence/absence data). The metric and its MLE, alpha hat, were advanced in 
  Mainali, Slud, et al, 2021 <doi:10.1126/sciadv.abj9204>. Various types of confidence intervals and median interval
  were developed in Mainali and Slud, 2022 <doi:10.1101/2022.11.01.514801>.
	"""
	
	homepage = "https://github.com/kpmainali/CooccurrenceAffinity"
	cran = "CooccurrenceAffinity" 

	version("1.0", md5="b11ed526ae50ed573b4f2065ecf3be24")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biasedurn@2.0.9:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
