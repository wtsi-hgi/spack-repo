# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFreqpcr(RPackage):
	"""Estimates Allele Frequency on qPCR DeltaDeltaCq from Bulk
Samples

	Interval estimation of the population allele frequency from qPCR analysis based on the restriction enzyme digestion (RED)-DeltaDeltaCq method (Osakabe et al. 2017, <doi:10.1016/j.pestbp.2017.04.003>), as well as general DeltaDeltaCq analysis. Compatible with the Cq measurement of DNA extracted from multiple individuals at once, so called "group-testing", this model assumes that the quantity of DNA extracted from an individual organism follows a gamma distribution. Therefore, the point estimate is robust regarding the uncertainty of the DNA yield.
	"""
	
	homepage = "https://github.com/sudoms/freqpcr"
	cran = "freqpcr" 

	version("0.4.0", md5="8b1001037c7f99d910345dcfec1d1892")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
