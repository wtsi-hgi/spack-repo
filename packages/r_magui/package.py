# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMagui(RPackage):
	"""A Graphical User Interface for Microarray Data Analysis and
Annotation

	Provides a comprehensive graphical user interface for analysis of Affymetrix, Agilent, Illumina, Nimblegen and other microarray data. It can perform miscellaneous tasks such as gene set enrichment and test analyses, identifying gene symbols and building co-expression network. It can also estimate sample size for atleast two-fold expression change. The current version is its slenderized form for compatable and flexible implementation.
	"""
	
	cran = "maGUI" 

	version("4.0", md5="04e3e52d034889573140164b69b7c127")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("tktable@2.10:", type=("build", "link", "run"))
