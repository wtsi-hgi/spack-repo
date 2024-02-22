# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGfiextremes(RPackage):
	"""Generalized Fiducial Inference for Extremes

	Fiducial framework to perform inference on the quantiles for a generalized Pareto distribution model and on the parameters of the Pareto exceedance distribution, assuming the exceedance threshold is a known or unknown parameter. Reference: Damian V. Wandler & Jan Hannig (2012) <doi:10.1007/s10687-011-0127-9>.
	"""
	
	homepage = "https://github.com/stla/gfiExtremes"
	cran = "gfiExtremes" 

	version("1.0.1", md5="395e67193b9f720d2da4f8f92e2b2091")

	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
