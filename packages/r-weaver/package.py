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

    version("1.74.0", tag="RELEASE_3_21")
	version("1.68.0", sha256="f9c2548dcad9d23a952dd8e9650fd690679a3f7f37ec20ca04cfa35d99cf7ff8")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
