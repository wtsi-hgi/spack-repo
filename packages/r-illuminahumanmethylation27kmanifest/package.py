# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminahumanmethylation27kmanifest(RPackage):
	"""Annotation for Illumina's 27k methylation arrays

	Manifest for Illumina's 27k array data
	"""
	
	bioc = "IlluminaHumanMethylation27kmanifest" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/IlluminaHumanMethylation27kmanifest_0.4.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/IlluminaHumanMethylation27kmanifest/IlluminaHumanMethylation27kmanifest_0.4.0.tar.gz"]

	version("0.4.0", md5="c4cdda637dccf85f193342c7262b02a6")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))

	# annotation