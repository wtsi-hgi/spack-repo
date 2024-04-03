# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminahumanmethylation450kmanifest(RPackage):
	"""Annotation for Illumina's 450k methylation arrays."""

	bioc = "IlluminaHumanMethylation450kmanifest"
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/IlluminaHumanMethylation450kmanifest_0.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/IlluminaHumanMethylation450kmanifest/IlluminaHumanMethylation450kmanifest_0.4.0.tar.gz"]
	
	version("0.4.0", md5="664d1f5a3892974334faa26757269509")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))

	# annotation