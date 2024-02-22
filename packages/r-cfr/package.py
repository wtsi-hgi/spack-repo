# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCfr(RPackage):
	"""Estimate Disease Severity and Case Ascertainment

	Estimate the severity of a disease and ascertainment of cases, as discussed in Nishiura et al. (2009) <doi:10.1371/journal.pone.0006852>.
	"""
	
	homepage = "https://github.com/epiverse-trace/cfr"
	cran = "cfr" 

	version("0.1.0", md5="839990122dd3e86944f530ce006787f1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
