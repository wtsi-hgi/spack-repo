# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuexexonprobesetlocationhg18(RPackage):
	"""Exon-level probeset chromosome location for microarrays of type HuEx

	This package was automatically created by package AnnotationDbi version 1.8.0. The exon-level probeset genome location was retrieved from Netaffx using AffyCompatible. The exon-level probeset genome location was retrieved from Netaffx using AffyCompatible. Genome release hg18.
	"""
	
	bioc = "HuExExonProbesetLocationHg18" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/HuExExonProbesetLocationHg18_0.0.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/HuExExonProbesetLocationHg18/HuExExonProbesetLocationHg18_0.0.2.tar.gz"]

	version("0.0.2", sha256="2fc903d7d581fa806b99eeebbaad6f6ddbf2ec3c8f8856c47ed9980016ab8b92", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/HuExExonProbesetLocationHg18_0.0.2.tar.gz")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.8:", type=("build", "run"))

