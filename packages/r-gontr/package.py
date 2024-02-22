# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGontr(RPackage):
	"""Dataset for 'GOxploreR'

	Contains the Gene ontology terms and skeleton for the reduced GO directed acyclic graph (DAG) for the organisms
             Rat and Mouse. The methods are explicitly discussed in the following article : Manjang et al (2020) <doi:10.1038/s41598-020-73326-3>.
	"""
	
	cran = "gontr" 

	version("1.1.0", md5="01d08fcf7c181ec8f3b69151d9948d99")

	depends_on("r@2.10:", type=("build", "run"))
