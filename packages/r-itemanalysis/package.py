# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RItemanalysis(RPackage):
	"""Classical Test Theory Item Analysis

	Runs classical item analysis for multiple-choice test items and polytomous items (e.g., rating scales). The statistics reported in this package can be found in any measurement textbook such as Crocker and Algina (2006, ISBN:9780495395911).
	"""
	
	homepage = "https://cengiz.me/"
	cran = "itemanalysis" 

	version("1.1", md5="7ba4c89da572f5fe9c219b90dfab1e30")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-polycor", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
