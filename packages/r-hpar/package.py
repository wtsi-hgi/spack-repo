# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHpar(RPackage):
	"""Human Protein Atlas in R

	The hpar package provides a simple R interface to and data from the Human Protein Atlas project.
	"""
	
	bioc = "hpar" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/hpar_1.44.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/hpar/hpar_1.44.0.tar.gz"]

	version("1.44.0", md5="f970b068a2112cd8bf1a8dfb7d29d86a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
