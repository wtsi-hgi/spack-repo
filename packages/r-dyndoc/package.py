# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDyndoc(RPackage):
	"""Dynamic document tools

	A set of functions to create and interact with dynamic documents and vignettes.
	"""
	
	bioc = "DynDoc" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DynDoc_1.80.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DynDoc/DynDoc_1.80.0.tar.gz"]

	version("1.80.0", sha256="c115174fcf50197ccb7b57d90f48b7a354707e687093e70f89371fffb5ea4a34")

