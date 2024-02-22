# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimilarpeak(RPackage):
	"""Metrics to estimate a level of similarity between two ChIP-Seq profiles

	This package calculates metrics which quantify the level of similarity between ChIP-Seq profiles. More specifically, the package implements six pseudometrics specialized in pattern similarity detection in ChIP-Seq profiles.
	"""
	
	homepage = "https://github.com/adeschen/similaRpeak"
	bioc = "similaRpeak" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/similaRpeak_1.34.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/similaRpeak/similaRpeak_1.34.0.tar.gz"]

	version("1.34.0", md5="3d91ba41941b12c9f93e77872e444c4d")

	depends_on("r-r6@2:", type=("build", "run"))
