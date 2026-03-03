# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCloneseeker(RPackage):
	"""Seeking and Finding Clones in Copy Number and Sequencing Data

	Defines the classes and functions used to simulate and
  to analyze data sets describing copy number variants and,
  optionally, sequencing mutations in order to detect clonal subsets.
  See Zucker et al. (2019) <doi:10.1093/bioinformatics/btz057>.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "CloneSeeker" 

	version("1.0.11", md5="d814e3183c5f25a07b391278d3b310f9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-mc2d", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
