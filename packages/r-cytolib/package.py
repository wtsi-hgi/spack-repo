# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytolib(RPackage):
	"""C++ infrastructure for representing and interacting with the gated cytometry data

	This package provides the core data structure and API to represent and interact with the gated cytometry data.
	"""
	
	bioc = "cytolib" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cytolib_2.14.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cytolib/cytolib_2.14.1.tar.gz"]

	version("2.14.1", sha256="2e37fafbf76a16720fb9b5df611df77d511420fd1f2f11431d94b536d28c4fcd")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rprotobuflib@2.13.1:", type=("build", "run"))
	depends_on("r-bh@1.84:", type=("build", "run"))
	depends_on("r-rhdf5lib", type=("build", "run"))
