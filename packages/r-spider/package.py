# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpider(RPackage):
	"""Species Identity and Evolution in R

	Analysis of species limits and DNA barcoding data. Included are functions for generating important summary statistics from DNA barcode data, assessing specimen identification efficacy, testing and optimizing divergence threshold limits, assessment of diagnostic nucleotides, and calculation of the probability of reciprocal monophyly. Additionally, a sliding window function offers opportunities to analyse information across a gene, often used for marker design in degraded DNA studies. Further information on the package has been published in Brown et al (2012) <doi:10.1111/j.1755-0998.2011.03108.x>.
	"""
	
	cran = "spider" 

	version("1.5.0", md5="6358834af6fe22434ac7b327ddea9954")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-pegas", type=("build", "run"))
