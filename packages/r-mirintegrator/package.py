# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirintegrator(RPackage):
	"""Integrating microRNA expression into signaling pathways for pathway analysis

	Tools for augmenting signaling pathways to perform pathway analysis of microRNA and mRNA expression levels.
	"""
	
	homepage = "http://datad.github.io/mirIntegrator/"
	bioc = "mirIntegrator" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/mirIntegrator_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/mirIntegrator/mirIntegrator_1.32.0.tar.gz"]

    version("1.38.0", tag="RELEASE_3_21")
	version("1.32.0", sha256="d109e9bebc6a1d74353260b70d4bd0c30b5f63f02c046b26e2122876d2f4edf2")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rontotools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
