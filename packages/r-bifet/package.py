# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBifet(RPackage):
	"""Bias-free Footprint Enrichment Test

	BiFET identifies TFs whose footprints are over-represented in target regions compared to background regions after correcting for the bias arising from the imbalance in read counts and GC contents between the target and background regions. For a given TF k, BiFET tests the null hypothesis that the target regions have the same probability of having footprints for the TF k as the background regions while correcting for the read count and GC content bias. For this, we use the number of target regions with footprints for TF k, t_k as a test statistic and calculate the p-value as the probability of observing t_k or more target regions with footprints under the null hypothesis.
	"""
	
	bioc = "BiFET"

	version("1.28.0", commit="2f2e0cd5413dcef23e498f17889f8d0ba1ca62d6")
	version("1.22.0", commit="b50b566019b3c08ad99e808913be8d760297aefe")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-poibin", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
