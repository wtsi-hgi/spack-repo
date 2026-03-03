# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArds(RPackage):
	"""Creates Analysis Results Datasets

	Contains functions to help create an Analysis Results Dataset.
    The dataset follows industry recommended structure.  The dataset can be 
    created in multiple passes, using different data frames as input.  Analysis
    Results Datasets are used in the pharmaceutical and biotech industries
    to capture analysis in a common tabular data structure.
	"""
	
	homepage = "https://ards.r-sassy.org"
	cran = "ards" 

	version("0.1.1", md5="49530bfc79eb54d3de1daa65581c8025")

	depends_on("r@4.1:", type=("build", "run"))
