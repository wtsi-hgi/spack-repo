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

	version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="64f51d7bd764d77341ecd641c9edc2844299789baaeee7cb75044d12e31e29f2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
