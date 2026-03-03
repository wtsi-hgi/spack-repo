# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErrors(RPackage):
	"""Uncertainty Propagation for R Vectors

	Support for measurement errors in R vectors, matrices and arrays:
    automatic uncertainty propagation and reporting.
    Documentation about 'errors' is provided in the paper by Ucar, Pebesma &
    Azcorra (2018, <doi:10.32614/RJ-2018-075>), included in this package as a
    vignette; see 'citation("errors")' for details.
	"""
	
	homepage = "https://r-quantities.github.io/errors/"
	cran = "errors" 

	version("0.4.1", md5="b72bb04bda04134a14e35f3ef70788d5")

	depends_on("r@3:", type=("build", "run"))
