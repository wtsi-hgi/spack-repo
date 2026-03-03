# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRabi(RPackage):
	"""Generate Codes to Uniquely and Robustly Identify Individuals for
Animal Behavior Studies

	Facilitates the design and generation of optimal color (or symbol) codes that can be used to mark and identify individual animals. These codes are made such that the IDs are robust to partial erasure: even if sections of the code are lost, the entire identity of the animal can be reconstructed. Thus, animal subjects are not confused and no ambiguity is introduced.
	"""
	
	cran = "rabi" 

	version("1.0.2", md5="5e8a5eaa9a8e7f7c48ff2b51438e2f86")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
