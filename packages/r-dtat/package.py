# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtat(RPackage):
	"""Dose Titration Algorithm Tuning

	Dose Titration Algorithm Tuning (DTAT) is a methodologic framework
             allowing dose individualization to be conceived as a continuous
             learning process that begins in early-phase clinical trials and
             continues throughout drug development, on into clinical practice.
             This package includes code that researchers may use to reproduce
             or extend key results of the DTAT research programme, plus tools
             for trialists to design and simulate a '3+3/PC' dose-finding study.
             Please see Norris (2017a) <doi:10.12688/f1000research.10624.3> and
             Norris (2017c) <doi:10.1101/240846>.
	"""
	
	homepage = "https://precisionmethods.guru/"
	cran = "DTAT" 

	version("0.3-6", md5="871740c7dc3b4da3b996e26e4a5125ee")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-km-ci", type=("build", "run"))
	depends_on("r-pomp", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-r2d3", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
