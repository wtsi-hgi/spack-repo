# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHumancytosnp12v2p1hcrlmm(RPackage):
	"""Metadata for fast genotyping with the 'crlmm' package

	Package with metadata for genotyping Illumina CytoSNP 12 arrays using the 'crlmm' package.
	"""
	
	bioc = "humancytosnp12v2p1hCrlmm" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/humancytosnp12v2p1hCrlmm_1.0.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/humancytosnp12v2p1hCrlmm/humancytosnp12v2p1hCrlmm_1.0.1.tar.gz"]

	version("1.0.1", sha256="5820dd56fc6628a9f5e2eefde2ae458d15f36d0e96c727da078523d935f649ac")


