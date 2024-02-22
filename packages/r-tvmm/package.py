# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTvmm(RPackage):
	"""Multivariate Tests for the Vector of Means

	This is a statistical tool interactive that provides multivariate statistical tests that are more powerful than traditional Hotelling T2 test and LRT (likelihood ratio test) for the vector of normal mean populations with and without contamination and non-normal populations (Henrique J. P. Alves & Daniel F. Ferreira (2019) <DOI: 10.1080/03610918.2019.1693596>).
	"""
	
	cran = "TVMM" 

	version("3.2.1", md5="b42078eb60ecd1b2b7c472c1cdfd9f8c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-tcltk2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-desctoolsaddins", type=("build", "run"))
