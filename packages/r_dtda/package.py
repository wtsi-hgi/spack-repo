# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtda(RPackage):
	"""Doubly Truncated Data Analysis

	Implementation of different algorithms for analyzing
        randomly truncated data, one-sided and two-sided (i.e. doubly)
        truncated data. It serves to compute empirical cumulative 
        distributions and also kernel density and hazard functions 
        using different bandwidth selectors.
      Several real data sets are included.
	"""
	
	cran = "DTDA" 

	version("3.0.1", md5="9de318d348aca64645df42f3ca28eaf4")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
