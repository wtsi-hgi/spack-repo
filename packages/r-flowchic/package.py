# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowchic(RPackage):
	"""Analyze flow cytometric data using histogram information

	A package to analyze flow cytometric data of complex microbial communities based on histogram images
	"""
	
	homepage = "http://www.ufz.de/index.php?en=16773"
	bioc = "flowCHIC" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowCHIC_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowCHIC/flowCHIC_1.36.0.tar.gz"]

    version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="e558421e260c2464482852ecada34e2c9972cf7afcf7f9be1f9e48069a0ccb69")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
