# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuexexonprobesetlocation(RPackage):
	"""Probe sequence data for microarrays of type HuEx

	This package was automatically created by package AnnotationForge version 1.7.17. The exon-level probeset genome location was retrieved from Netaffx using AffyCompatible.
	"""
	
	bioc = "HuExExonProbesetLocation" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/HuExExonProbesetLocation_1.15.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/HuExExonProbesetLocation/HuExExonProbesetLocation_1.15.0.tar.gz"]

	version("1.15.0", md5="11bf1b88d9e90711b4064497f611da4f")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.7.17:", type=("build", "run"))

	# annotation