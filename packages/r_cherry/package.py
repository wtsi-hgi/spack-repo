# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCherry(RPackage):
	"""Multiple Testing Methods for Exploratory Research

	Provides an alternative approach to multiple testing
        by calculating a simultaneous upper confidence bounds for the
        number of true null hypotheses among any subset of the hypotheses of interest, 
        using the methods of Goeman and Solari (2011) <doi:10.1214/11-STS356>. 
	"""
	
	cran = "cherry" 

	version("0.6-14", md5="539c99dea5123931eff058ac6bc53cea")

	depends_on("r-bitops", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-hommel", type=("build", "run"))
