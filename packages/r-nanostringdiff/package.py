# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNanostringdiff(RPackage):
	"""Differential Expression Analysis of NanoString nCounter Data

	This Package utilizes a generalized linear model(GLM) of the negative binomial family to characterize count data and allows for multi-factor design. NanoStrongDiff incorporate size factors, calculated from positive controls and housekeeping controls, and background level, obtained from negative controls, in the model framework so that all the normalization information provided by NanoString nCounter Analyzer is fully utilized.
	"""
	
	bioc = "NanoStringDiff"

	version("1.38.0", commit="c2d837227c454a0b4234d989ccd5d47732c23db7")
	version("1.32.0", commit="4afdd7f06cdf5b685b7a2b40ec11eeda038dc493")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
