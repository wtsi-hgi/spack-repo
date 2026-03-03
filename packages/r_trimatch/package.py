# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrimatch(RPackage):
	"""Propensity Score Matching of Non-Binary Treatments

	Propensity score matching for non-binary treatments.
	"""
	
	homepage = "http://jason.bryer.org/TriMatch"
	cran = "TriMatch" 

	version("0.9.9", md5="cd8deca729c70408ae868bf6bfd9f79c")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ez", type=("build", "run"))
	depends_on("r@3:", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-psagraphics", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
