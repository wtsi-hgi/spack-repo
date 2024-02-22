# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTuneranger(RPackage):
	"""Tune Random Forest of the 'ranger' Package

	Tuning random forest with one line. The package is mainly based on the packages 'ranger' and 'mlrMBO'.
	"""
	
	cran = "tuneRanger" 

	version("0.5", md5="c5f99d8031229c08c75277813a253699")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-ranger@0.8:", type=("build", "run"))
	depends_on("r-mlrmbo@1.1.1:", type=("build", "run"))
	depends_on("r-lubridate@1.6:", type=("build", "run"))
	depends_on("r-lhs@0.14:", type=("build", "run"))
	depends_on("r-mlr@2.11:", type=("build", "run"))
	depends_on("r-smoof@1.5.1:", type=("build", "run"))
	depends_on("r-paramhelpers@1.10:", type=("build", "run"))
	depends_on("r-bbmisc@1.11:", type=("build", "run"))
	depends_on("r-dicekriging@1.5.5:", type=("build", "run"))
