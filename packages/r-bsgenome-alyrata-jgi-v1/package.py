# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeAlyrataJgiV1(RPackage):
	"""Arabidopsis lyrata full genome (JGI version V1.0)

	Arabidopsis lyrata 8x Release [project ID 4002920] as provided by JGI ( snapshot from March 24, 2011) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Alyrata.JGI.v1" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Alyrata.JGI.v1_1.0.1.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/BSgenome.Alyrata.JGI.v1/BSgenome.Alyrata.JGI.v1_1.0.1.tar.gz"]

	version("1.0.1", md5="64878499c633de66ccf4c5abc32c0aeb", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/BSgenome.Alyrata.JGI.v1_1.0.1.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

	# annotation