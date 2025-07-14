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

    version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="2e6c3cb035628750f6b7f559cf276e5dd50d8ead73b08cdf635186a7342c6da1")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-igraph@0.7.1:", type=("build", "run"))
