# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataTree(RPackage):
	"""General Purpose Hierarchical Data Structure

	Create tree structures from hierarchical data, and traverse the
    tree in various orders. Aggregate, cumulate, print, plot, convert to and from
    data.frame and more. Useful for decision trees, machine learning, finance,
    conversion from and to JSON, and many other applications.
	"""
	
	homepage = "https://github.com/gluc/data.tree"
	cran = "data.tree" 

	version("1.1.0", md5="2cb316683cdf181900d26e49b69d7f79")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
