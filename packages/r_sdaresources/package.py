# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdaresources(RPackage):
	"""Datasets and Functions for 'Sampling: Design and Analysis, 3rd
Edition'

	Includes all the datasets of 'Sampling: Design and Analysis'
    (3rd edition by Sharon Lohr) in R format and additional functions for
    analyzing and graphing probability samples.
	"""
	
	cran = "SDAResources" 

	version("0.1.1", md5="c2c6ffb4d633a7a0444e4d770d5385d6")

	depends_on("r@3.5:", type=("build", "run"))
