# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFamilies(RPackage):
	"""Kinship Ties in Virtual Populations

	Tools to study kinship networks, grandparenthood, and double burden (presence of children and oldest old parents) in virtual population produced by 'VirtualPop'.
	"""
	
	cran = "Families" 

	version("1.0.1", md5="8e006a7d5f60c512aae9d3f08cf86188")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
