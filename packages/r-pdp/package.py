# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdp(RPackage):
	"""Partial Dependence Plots

	A general framework for constructing partial dependence (i.e.,
        marginal effect) plots from various types machine learning models
        in R.
	"""
	
	homepage = "https://github.com/bgreenwell/pdp"
	cran = "pdp" 

	version("0.8.1", md5="4166dcbdd133194280260675aa63dfee")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
