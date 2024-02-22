# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProbedeveloper(RPackage):
	"""Develop Hybridization Probes

	Hybridization probes for target sequences can be made based on melting temperature value calculated by R package 'TmCalculator' <https://CRAN.R-project.org/package=TmCalculator> and methods extended from Beliveau, B. J.,(2018) <doi:10.1073/pnas.1714530115>, and those hybridization probes can be used to capture specific target regions in fluorescence in situ hybridization and next generation sequence experiments.
	"""
	
	cran = "ProbeDeveloper" 

	version("1.1.0", md5="1a80269f08cf20b1092859c377f1f37b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tmcalculator@1.0.2:", type=("build", "run"))
	depends_on("r-biostrings@2.12:", type=("build", "run"))
