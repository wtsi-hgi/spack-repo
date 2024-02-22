# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcchoice(RPackage):
	"""Analyzing Dichotomous Choice Contingent Valuation Data

	Functions for analyzing dichotomous choice contingent 
   valuation (CV) data. It provides functions for estimating parametric and 
   nonparametric models for single-, one-and-one-half-, and double-bounded 
   CV data. For details, see Aizaki et al. (2022) <doi:10.1007/s42081-022-00171-1>.
	"""
	
	homepage = "http://www.agr.hokudai.ac.jp/spmur/"
	cran = "DCchoice" 

	version("0.2.0", md5="e6ad43428fc680b0c892bf1c8f2b9c3a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-interval", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
