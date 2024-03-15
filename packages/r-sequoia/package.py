# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSequoia(RPackage):
	"""Pedigree Inference from SNPs

	Multi-generational pedigree inference from incomplete data on
    hundreds of SNPs, including parentage assignment and sibship clustering.
    See Huisman (2017) (<DOI:10.1111/1755-0998.12665>) for more information.
	"""
	
	homepage = "https://jiscah.github.io/"
	cran = "sequoia" 

	version("2.9.0", md5="dc25281058eba695694d8a8c9b6ffd18")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plyr@1.8:", type=("build", "run"))
