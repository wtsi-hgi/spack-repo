# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChor(RPackage):
	"""Chordalysis R Package

	
    Learning the structure of graphical models from datasets with thousands of variables.
    More information about the research papers detailing the theory behind Chordalysis is available at
    <http://www.francois-petitjean.com/Research> (KDD 2016, SDM 2015, ICDM 2014, ICDM 2013).
    The R package development site is <https://github.com/HerrmannM/Monash-ChoR>.
	"""
	
	cran = "ChoR" 

	version("0.0-4", md5="c038cfa5ef7bef6cc71f885ed7512f33")

	depends_on("r-rjava@0.9.9:", type=("build", "run"))
	depends_on("r-commonsmath", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
