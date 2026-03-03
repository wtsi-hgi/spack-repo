# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcensmix(RPackage):
	"""Model Fitting to Progressively Censored Mixture Data

	Functions for generating progressively Type-II censored data in
    a mixture structure and fitting models using a constrained EM algorithm. It can also
    create a progressive Type-II censored version of a given real dataset to be considered for
    model fitting. 
	"""
	
	cran = "pcensmix" 

	version("1.2-1", md5="8e45fd8699463c33134eaf4e8253c742")

	depends_on("r@3.3.3:", type=("build", "run"))
