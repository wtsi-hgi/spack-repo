# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConsort(RPackage):
	"""Create Consort Diagram

	To make it easy to create CONSORT diagrams for the transparent reporting of participant allocation in randomized, controlled clinical trials. This is done by creating a standardized disposition data, and using this data as the source for the creation a standard CONSORT diagram. Human effort by supplying text labels on the node can also be achieved.
	"""
	
	homepage = "https://github.com/adayim/consort/"
	cran = "consort" 

	version("1.2.1", md5="5a82816d70848f3143ff65cea7303fd5")

	depends_on("r@3.5:", type=("build", "run"))
