# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQfasar(RPackage):
	"""Quantitative Fatty Acid Signature Analysis in R

	An implementation of Quantitative Fatty Acid Signature
    Analysis (QFASA) in R.  QFASA is a method of estimating the diet
    composition of predators.  The fundamental unit of information in
    QFASA is a fatty acid signature (signature), which is a vector of
    proportions describing the composition of fatty acids within lipids.
    Signature data from at least one predator and from samples of all
    potential prey types are required.  Calibration coefficients, which
    adjust for the differential metabolism of individual fatty acids by
    predators, are also required. Given those data inputs, a predator
    signature is modeled as a mixture of prey signatures and its diet
    estimate is obtained as the mixture that minimizes a measure of
    distance between the observed and modeled signatures.  A variety of
    estimation options and simulation capabilities are implemented.
    Please refer to the vignette for additional details and references.
	"""
	
	cran = "qfasar" 

	version("1.2.1", md5="1f852999996108a73bb5208bb6df8207")

	depends_on("r-rsolnp@1.16:", type=("build", "run"))
