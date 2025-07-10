# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RObmiti(RPackage):
	"""Ob/ob Mice Data on Normal and High Fat Diet

	The package provide RNA-seq count for 2 strains of mus musclus; Wild type and Ob/Ob. Each strain was divided into two groups, and each group received either chow diet or high fat diet. RNA expression was measured after 20 weeks in 7 tissues.
	"""
	
	homepage = "https://github.com/OmarElAshkar/ObMiTi"
	bioc = "ObMiTi" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/ObMiTi_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/ObMiTi/ObMiTi_1.10.0.tar.gz"]

	version("1.10.0", sha256="df02da0d6e339de1a22dc9c6fd826b0afe5672d2f7096b7cac296dbb2a1af4e9")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

