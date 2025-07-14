# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROncoscore(RPackage):
	"""A tool to identify potentially oncogenic genes

	OncoScore is a tool to measure the association of genes to cancer based on citation frequencies in biomedical literature. The score is evaluated from PubMed literature by dynamically updatable web queries.
	"""
	
	homepage = "https://github.com/danro9685/OncoScore"
	bioc = "OncoScore"

	version("1.36.0", commit="b83a0ddd141f21fad7fc51e81dc39a38f70c28fc")
	version("1.30.0", commit="8bbdd2a168209777954f811262b74c99fc44ffde")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
