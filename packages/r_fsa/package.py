# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFsa(RPackage):
	"""Simple Fisheries Stock Assessment Methods

	A variety of simple fish stock assessment methods.
	"""
	
	homepage = "https://fishr-core-team.github.io/FSA/"
	cran = "FSA" 

	version("0.9.5", md5="54f643addaac3d904cb79d0ea5d6c895")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-dunn-test", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
