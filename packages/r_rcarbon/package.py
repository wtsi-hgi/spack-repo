# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcarbon(RPackage):
	"""Calibration and Analysis of Radiocarbon Dates

	Enables the calibration and analysis of radiocarbon dates, often but not exclusively for the purposes of archaeological research. It includes functions not only for basic calibration, uncalibration, and plotting of one or more dates, but also a statistical framework for building demographic and related longitudinal inferences from aggregate radiocarbon date lists, including: Monte-Carlo simulation test (Timpson et al 2014 <doi:10.1016/j.jas.2014.08.011>), random mark permutation test (Crema et al 2016 <doi:10.1371/journal.pone.0154809>) and spatial permutation tests (Crema, Bevan, and Shennan 2017 <doi:10.1016/j.jas.2017.09.007>).  
	"""
	
	homepage = "https://github.com/ahb108/rcarbon/"
	cran = "rcarbon" 

	version("1.5.1", md5="a8115db4ba6fcd10bab974449ca3b7cc")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-model", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-linnet", type=("build", "run"))
	depends_on("r-spatstat@2.0.0:", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
