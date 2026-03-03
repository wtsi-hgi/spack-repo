# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlindreview(RPackage):
	"""Enables Blind Review of Database

	Randomly reassigns the group identifications to one of the variables of the 
   database, say Treatment, and randomly reassigns the observation numbers of the dataset. 
   Reorders the observations according to these new numbers. Centers each group of Treatment
   at the grand mean in order to further mask the treatment. An unmasking function is 
   provided so that the user can identify the potential outliers in terms of their original 
   values when blinding is no longer needed. It is suggested that a forward search procedure 
   be performed on the masked data. Details of some forward search functions may be found in
   <https://CRAN.R-project.org/package=forsearch>.
	"""
	
	cran = "blindreview" 

	version("2.0.0", md5="3239d4fb4d0681e606a0d788d0a48800")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-hmisc@4.7.2:", type=("build", "run"))
	depends_on("gmp@4.1:", type=("build", "link", "run"))
