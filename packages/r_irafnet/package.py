# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrafnet(RPackage):
	"""Integrative Random Forest for Gene Regulatory Network Inference

	Provides a flexible integrative algorithm that allows information from prior data, such as protein protein interactions and gene knock-down, to be jointly considered for gene regulatory network inference.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "iRafNet" 

	version("1.1-1", md5="6f7606a8b873322fd59825cbfa78c39a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
