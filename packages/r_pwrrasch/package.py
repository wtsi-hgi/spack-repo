# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwrrasch(RPackage):
	"""Statistical Power Simulation for Testing the Rasch Model

	Statistical power simulation for testing the Rasch Model based on a three-way analysis of variance design with mixed classification.
	"""
	
	cran = "pwrRasch" 

	version("0.1-2", md5="1e6fa91c3fed9122ab1af0a09fddfe22")

	depends_on("r@3:", type=("build", "run"))
