# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIat(RPackage):
	"""Cleaning and Visualizing Implicit Association Test (IAT) Data

	Implements the standard D-Scoring algorithm
    (Greenwald, Banaji, & Nosek, 2003) for Implicit Association Test (IAT)
    data and includes plotting capabilities for exploring raw IAT data.
	"""
	
	cran = "IAT" 

	version("0.3", md5="46822e4bc6fe6926b316180dcf54e325")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-dplyr@0.4.3:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-lazyeval@0.1.10:", type=("build", "run"))
