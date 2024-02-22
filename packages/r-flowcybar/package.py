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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/flowCyBar_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/flowCyBar/flowCyBar_1.38.0.tar.gz"]

	version("1.38.0", md5="9236c02598960d4536906fb7449a7dd4")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
