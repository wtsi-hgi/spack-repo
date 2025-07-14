# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArrmnormalization(RPackage):
	"""Adaptive Robust Regression normalization for Illumina methylation data

	Perform the Adaptive Robust Regression method (ARRm) for the normalization of methylation data from the Illumina Infinium HumanMethylation 450k assay.
	"""
	
	bioc = "ARRmNormalization"

	version("1.48.0", commit="ec7bdf155db4410abba836a003bf8eeecfb90bc6")
	version("1.42.0", commit="201a902c0a814c145a77f68d98b89abb91065dce")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-arrmdata", type=("build", "run"))
