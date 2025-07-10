# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultimed(RPackage):
	"""Testing multiple biological mediators simultaneously

	Implements methods for testing multiple mediators
	"""
	
	bioc = "MultiMed" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MultiMed_2.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MultiMed/MultiMed_2.24.0.tar.gz"]

	version("2.24.0", sha256="9904ecf3cd672505b4789252deb363db51d8150c3c71ecc73b5f34aa3c86ae3b")

	depends_on("r@3.1:", type=("build", "run"))
