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

	version("1.44.0", commit="861cd52143281f79635dbfcfaf9f163316254593")
	version("1.38.0", commit="5784d61795ae1e4050f289e580fcba72bd133b8a")

	depends_on("r@2.10:", type=("build", "run"))

