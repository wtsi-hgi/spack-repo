# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBalli(RPackage):
	"""Expression RNA-Seq Data Analysis Based on Linear Mixed Model

	Analysis of gene expression RNA-seq data using Bartlett-Adjusted Likelihood-based LInear model (BALLI). Based on likelihood ratio test, it provides comparisons for effect of one or more variables. See Kyungtaek Park (2018) <doi:10.1101/344929> for more information. 
	"""
	
	cran = "BALLI" 

	version("0.2.0", md5="c01d069edd3b6cd255768fe0718ad899")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
