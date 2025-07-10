# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsgenomeOsativaMsuMsu7(RPackage):
	"""Oryza sativa full genome (MSU7)

	Oryza sativa full genome as provided by MSU (MSU7 Genome Release) and stored in Biostrings objects.
	"""
	
	bioc = "BSgenome.Osativa.MSU.MSU7" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Osativa.MSU.MSU7_0.99.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/BSgenome.Osativa.MSU.MSU7/BSgenome.Osativa.MSU.MSU7_0.99.2.tar.gz"]

	version("0.99.2", sha256="71275d58909c14c3de10c1846fc2e8c3c2555990a24922586e2624264c9cf7e6", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/BSgenome.Osativa.MSU.MSU7_0.99.2.tar.gz")

	depends_on("r-bsgenome", type=("build", "run"))

