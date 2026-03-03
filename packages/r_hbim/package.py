# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHbim(RPackage):
	"""Hill/Bliss Independence Model for Combination Vaccines

	Calculate expected relative risk and proportion protected assuming normally distributed log10 transformed antibody dose for a several component vaccine. Uses Hill models for each component which are combined under Bliss independence. See Saul and Fay, 2007 <DOI:10.1371/journal.pone.0000850>. 
	"""
	
	cran = "hbim" 

	version("1.1.2", md5="78586eb432e37006c6b196fdd255a425")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
