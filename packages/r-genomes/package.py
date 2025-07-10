# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomes(RPackage):
	"""Genome sequencing project metadata

	Download genome and assembly reports from NCBI
	"""
	
	bioc = "genomes" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/genomes_3.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/genomes/genomes_3.32.0.tar.gz"]

	version("3.32.0", sha256="054df747ef956fdbb6acbb20417216c5114f4a0960d274e88c34fc73fb60cf0f")

	depends_on("r-readr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
