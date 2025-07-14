# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCohcapanno(RPackage):
	"""Annotations for City of Hope CpG Island Analysis Pipeline

	Provides genomic location, nearby CpG island and nearby gene information for common Illumina methylation array platforms
	"""
	
	bioc = "COHCAPanno" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/COHCAPanno_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/COHCAPanno/COHCAPanno_1.38.0.tar.gz"]

    version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="0362bd4a6d984f5748613751d4b525d6580e360d61d60bc625617d4855a10539")

	depends_on("r@2.10:", type=("build", "run"))

