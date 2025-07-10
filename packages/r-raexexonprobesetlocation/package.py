# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaexexonprobesetlocation(RPackage):
	"""Probe sequence data for microarrays of type RaEx

	This package was automatically created by package AnnotationForge version 1.7.17. The exon-level probeset genome location was retrieved from Netaffx using AffyCompatible.
	"""
	
	bioc = "RaExExonProbesetLocation" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/RaExExonProbesetLocation_1.15.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/RaExExonProbesetLocation/RaExExonProbesetLocation_1.15.0.tar.gz"]

	version("1.15.0", sha256="0d0e9a7bd324446bc155e242b879307a48819ae7be0b4fa6c276bd4b7f616cef")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.7.17:", type=("build", "run"))

