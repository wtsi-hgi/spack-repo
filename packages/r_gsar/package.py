# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsar(RPackage):
	"""Gene Set Analysis in R

	Gene set analysis using specific alternative hypotheses. Tests for differential expression, scale and net correlation structure.
	"""
	
	bioc = "GSAR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GSAR_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GSAR/GSAR_1.36.0.tar.gz"]

	version("1.36.0", md5="9828682d8721bde17ea31c9ed807174d")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-igraph@0.7.1:", type=("build", "run"))
