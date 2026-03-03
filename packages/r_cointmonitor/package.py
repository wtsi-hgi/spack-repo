# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCointmonitor(RPackage):
	"""Consistent Monitoring of Stationarity and Cointegrating
Relationships

	We propose a consistent monitoring procedure to detect a
    structural change from a cointegrating relationship to a spurious
    relationship. The procedure is based on residuals from modified least
    squares estimation, using either Fully Modified, Dynamic or Integrated
    Modified OLS. It is inspired by Chu et al. (1996) <DOI:10.2307/2171955> in
    that it is based on parameter estimation on a pre-break "calibration" period
    only, rather than being based on sequential estimation over the full sample.
    See the discussion paper <DOI:10.2139/ssrn.2624657> for further information.
    This package provides the monitoring procedures for both the cointegration
    and the stationarity case (while the latter is just a special case of the
    former one) as well as printing and plotting methods for a clear
    presentation of the results.
	"""
	
	homepage = "https://github.com/aschersleben/cointmonitoR"
	cran = "cointmonitoR" 

	version("0.1.0", md5="6d0b23dfe4bcd8b3ecbc1ddb386f291e")

	depends_on("r-cointreg@0.2:", type=("build", "run"))
	depends_on("r-matrixstats@0.14.1:", type=("build", "run"))
