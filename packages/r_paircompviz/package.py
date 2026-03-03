# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaircompviz(RPackage):
	"""Multiple comparison test visualization

	This package provides visualization of the results from the multiple (i.e. pairwise) comparison tests such as pairwise.t.test, pairwise.prop.test or pairwise.wilcox.test. The groups being compared are visualized as nodes in Hasse diagram. Such approach enables very clear and vivid depiction of which group is significantly greater than which others, especially if comparing a large number of groups.
	"""
	
	bioc = "paircompviz" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/paircompviz_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/paircompviz/paircompviz_1.40.0.tar.gz"]

	version("1.40.0", md5="e9c57c7305e15062d9258019fed12f3e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
