# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsea(RPackage):
	"""Simultaneous Enrichment Analysis

	SEA performs simultaneous feature-set testing for (gen)omics data. It tests the unified null hypothesis controls the family-wise error rate for all possible pathways. The unified null hypothesis is defined as: "The proportion of true features in the set is less than or equal to the threshold c", where c is selected by the user. Family-wise error rate control is provided through use of closed testing with Simes test. For more information on closed testing with Simes see Goeman et al. (2019) <doi:10.1093/biomet/asz041> and for more information about the properties and performance of SEA procedure see Ebrahimpoor et al. (2019) <doi:10.1093/bib/bbz074>.
	"""
	
	homepage = "https://github.com/mitra-ep/rSEA"
	cran = "rSEA" 

	version("2.1.1", md5="c973a852f46f42dfbf2a53ce0a317735")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-hommel@1.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
