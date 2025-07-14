# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowcybar(RPackage):
	"""Analyze flow cytometric data using gate information

	A package to analyze flow cytometric data using gate information to follow population/community dynamics
	"""
	
	homepage = "http://www.ufz.de/index.php?de=16773"
	bioc = "flowCyBar" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowCyBar_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowCyBar/flowCyBar_1.38.0.tar.gz"]

    version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="a129626e119624926cf56b60be2ddf4eaf8f03f8143433072a040f54384e987d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
