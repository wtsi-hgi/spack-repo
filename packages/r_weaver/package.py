# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeaver(RPackage):
	"""Tools and extensions for processing Sweave documents

	This package provides enhancements on the Sweave() function in the base package.  In particular a facility for caching code chunk results is included.
	"""
	
	bioc = "weaver" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/weaver_1.68.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/weaver/weaver_1.68.0.tar.gz"]

	version("1.68.0", md5="629d19681872923f14b50543d833c1ba")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
