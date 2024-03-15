# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnits(RPackage):
	"""Measurement Units for R Vectors.

	Support for measurement units in R vectors, matrices and arrays: automatic
	propagation, conversion, derivation and simplification of units; raising
	errors in case of unit incompatibility. Compatible with the POSIXct, Date
	and difftime  classes. Uses the UNIDATA udunits library and unit database
	for  unit compatibility checking and conversion. Documentation about
	'units' is provided in the paper by Pebesma, Mailund & Hiebert (2016,
	<doi:10.32614/RJ-2016-061>), included in this package as a vignette; see
	'citation("units")' for details."""

	cran = "units"

	license("GPL-2.0-only")

	version("0.8-5", md5="a6d32757cf3662c53fc43ba0eb7bef59")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp@0.12.10:", type=("build", "run"))
	depends_on("udunits@2:", type=("build", "link", "run"))
