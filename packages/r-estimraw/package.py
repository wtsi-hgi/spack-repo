# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REstimraw(RPackage):
	"""Estimation of Four-Fold Table Cell Frequencies (Raw Data) from
Effect Size Measures

	Estimation of four-fold table cell frequencies (raw data) from risk ratios (relative risks), risk differences and odds ratios. While raw data can be useful for doing meta-analysis, such data is often not provided by primary studies (with summary statistics being solely presented). Therefore, based on summary statistics (namely, risk ratios, risk differences and odds ratios), this package estimates the value of each cell in a 2x2 table according to the equations described in Di Pietrantonj C (2006) <doi:10.1002/sim.2287>.
	"""
	
	cran = "estimraw" 

	version("1.0.0", md5="b99a23b850febdf2f004256a812a18d2")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
