# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBacon(RPackage):
	"""Controlling bias and inflation in association studies using the empirical null distribution

	Bacon can be used to remove inflation and bias often observed in epigenome- and transcriptome-wide association studies. To this end bacon constructs an empirical null distribution using a Gibbs Sampling algorithm by fitting a three-component normal mixture on z-scores.
	"""
	
	bioc = "bacon" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/bacon_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/bacon/bacon_1.30.0.tar.gz"]

	version("1.30.0", md5="3757e896d5a8253845a21e37e555044a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
