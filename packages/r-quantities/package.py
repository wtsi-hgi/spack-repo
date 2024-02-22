# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantities(RPackage):
	"""Quantity Calculus for R Vectors

	Integration of the 'units' and 'errors' packages for a complete
    quantity calculus system for R vectors, matrices and arrays, with automatic
    propagation, conversion, derivation and simplification of magnitudes and
    uncertainties. Documentation about 'units' and 'errors' is provided in the
    papers by Pebesma, Mailund & Hiebert (2016, <doi:10.32614/RJ-2016-061>) and
    by Ucar, Pebesma & Azcorra (2018, <doi:10.32614/RJ-2018-075>), included in
    those packages as vignettes; see 'citation("quantities")' for details.
	"""
	
	homepage = "https://r-quantities.github.io/quantities/"
	cran = "quantities" 

	version("0.2.1", md5="00d01147d0f4581d3356280a88530392")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-units@0.8.0:", type=("build", "run"))
	depends_on("r-errors@0.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12.10:", type=("build", "run"))
