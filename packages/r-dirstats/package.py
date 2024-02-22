# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDirstats(RPackage):
	"""Nonparametric Methods for Directional Data

	Nonparametric kernel density estimation, bandwidth selection,
    and other utilities for analyzing directional data. Implements the estimator
    in Bai, Rao and Zhao (1987) <doi:10.1016/0047-259X(88)90113-3>, the
    cross-validation bandwidth selectors in Hall, Watson and Cabrera (1987)
    <doi:10.1093/biomet/74.4.751> and the plug-in bandwidth selectors in
    García-Portugués (2013) <doi:10.1214/13-ejs821>.
	"""
	
	homepage = "https://github.com/egarpor/DirStats"
	cran = "DirStats" 

	version("0.1.9", md5="e95da9e6616bb617fc20e2ebc76e9aee")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-movmf", type=("build", "run"))
	depends_on("r-rotasym", type=("build", "run"))
