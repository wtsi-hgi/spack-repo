# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColorednoise(RPackage):
	"""Simulate Temporally Autocorrelated Populations

	Temporally autocorrelated populations are correlated in their vital rates (growth, death, etc.) from year to year. It is very common for populations, whether they be bacteria, plants, or humans, to be temporally autocorrelated. This poses a challenge for stochastic population modeling, because a temporally correlated population will behave differently from an uncorrelated one.
    This package provides tools for simulating populations with white noise (no temporal autocorrelation), red noise (positive temporal autocorrelation), and blue noise (negative temporal autocorrelation).  The algebraic formulation for autocorrelated noise comes from Ruokolainen et al. (2009) <doi:10.1016/j.tree.2009.04.009>. Models for unstructured populations and for structured populations (matrix models) are available.
	"""
	
	cran = "colorednoise" 

	version("1.1.1", md5="0d296a299104453777a897dba1bc03a2")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-purrr@0.2.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
