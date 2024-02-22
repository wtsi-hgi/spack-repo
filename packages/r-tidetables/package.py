# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidetables(RPackage):
	"""Tide Analysis and Prediction of Predominantly Semi-Diurnal Tides

	Tide analysis and prediction of predominantly semi-diurnal tides
    with two high waters and two low waters during one lunar day (~24.842 hours,
    ~1.035 days). The analysis should preferably cover an observation period of at
    least 19 years. For shorter periods, for example, the nodal cycle can not be
    taken into account, which particularly affects the height calculation. The main
    objective of this package is to produce tide tables.
	"""
	
	cran = "TideTables" 

	version("0.0.3", md5="7e156a3d4f44a68b765308b607718394")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-chron@2.3.54:", type=("build", "run"))
	depends_on("r-data-table@1.13.2:", type=("build", "run"))
