# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfpredinterval(RPackage):
	"""Prediction Intervals with Random Forests and Boosted Forests

	Implements various prediction interval methods with random forests and boosted forests.
    The package has two main functions: pibf() produces prediction intervals with boosted forests
    (PIBF) as described in Alakus et al. (2022) <doi:10.32614/RJ-2022-012> and rfpi() builds 15
    distinct variations of prediction intervals with random forests (RFPI) proposed by Roy and
    Larocque (2020) <doi:10.1177/0962280219829885>.
	"""
	
	homepage = "https://github.com/calakus/RFpredInterval"
	cran = "RFpredInterval" 

	version("1.0.8", md5="ba2b10d4da5a2e4c872d21a7c0083dc2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-hdrcde", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
