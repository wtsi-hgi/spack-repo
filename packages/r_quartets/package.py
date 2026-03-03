# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuartets(RPackage):
	"""Datasets to Help Teach Statistics

	In the spirit of Anscombe's quartet, this package includes datasets
   that demonstrate the importance of visualizing your data, the importance of 
   not relying on statistical summary measures alone, and why additional 
   assumptions about the data generating mechanism are needed when estimating 
   causal effects. The package includes "Anscombe's Quartet" (Anscombe 1973) <doi:10.1080/00031305.1973.10478966>,
   D'Agostino McGowan & Barrett (2023) "Causal Quartet" <doi:10.48550/arXiv.2304.02683>, 
   "Datasaurus Dozen" (Matejka & Fitzmaurice 2017), "Interaction Triptych" (Rohrer & Arslan 2021) <doi:10.1177/25152459211007368>, "Rashomon Quartet" (Biecek et al. 2023) <doi:10.48550/arXiv.2302.13356>, and
   Gelman "Variation and Heterogeneity Causal Quartets" (Gelman et al. 2023) <doi:10.48550/arXiv.2302.12878>.
	"""
	
	homepage = "https://github.com/r-causal/quartets"
	cran = "quartets" 

	version("0.1.1", md5="ad194d660e3ce95a107e9a56404fba16")

	depends_on("r@2.10:", type=("build", "run"))
