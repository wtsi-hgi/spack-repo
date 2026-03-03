# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtbi(RPackage):
	"""A Procedure to Clean, Decompose and Aggregate Timeseries

	Clean, decompose and aggregate univariate time series following the procedure "Cyclic/trend decomposition using bin interpolation" and the Logbox method for flagging outliers, both detailed in Ritter, F.: Technical note: A procedure to clean, decompose, and aggregate time series, Hydrol. Earth Syst. Sci., 27, 349–361, <doi:10.5194/hess-27-349-2023>, 2023.
	"""
	
	homepage = "https://github.com/fritte2/ctbi"
	cran = "ctbi" 

	version("2.0.5", md5="e154258985c97bebceb3971cb500a0eb")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-data-table@1.14.2:", type=("build", "run"))
