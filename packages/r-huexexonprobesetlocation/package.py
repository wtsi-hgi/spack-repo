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
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/HuExExonProbesetLocation_1.15.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/HuExExonProbesetLocation/HuExExonProbesetLocation_1.15.0.tar.gz"]

	version("1.15.0", sha256="81574b061bfda24714e67d8cbb1fb73852db9bb7d8e559d28109be93204ff666")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.7.17:", type=("build", "run"))

