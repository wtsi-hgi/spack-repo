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

	version("1.38.0", md5="78fd4891651a8a62779fe402a13ba6b1")

	depends_on("r@2.10:", type=("build", "run"))

	# experiment