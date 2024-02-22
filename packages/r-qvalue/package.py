# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQvalue(RPackage):
	"""Q-value estimation for false discovery rate control.

	This package takes a list of p-values resulting from the simultaneous
	testing of many hypotheses and estimates their q-values and local FDR
	values. The q-value of a test measures the proportion of false positives
	incurred (called the false discovery rate) when that particular test is
	called significant. The local FDR measures the posterior probability the
	null hypothesis is true given the test's p-value. Various plots are
	automatically generated, allowing one to make sensible significance cut-
	offs. Several mathematical results have recently been shown on the
	conservative accuracy of the estimated q-values from this software. The
	software can be applied to problems in genomics, brain imaging,
	astrophysics, and data mining."""

	bioc = "qvalue"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/qvalue_2.34.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/qvalue/qvalue_2.34.0.tar.gz"]

	version("2.34.0", md5="d6d57a60a814587681cf438b4e6ee9bc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
