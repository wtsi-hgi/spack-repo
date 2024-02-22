# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsmrob(RPackage):
	"""Robust Estimation and Inference in Sample Selection Models

	Package provides a set of tools for robust estimation and inference for models with sample selectivity and endogenous treatment model. For details, see Zhelonkin and Ronchetti (2021) <doi:10.18637/jss.v099.i04>. 
	"""
	
	cran = "ssmrob" 

	version("1.0", md5="420308c79d470a7b7d444979471f990b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sampleselection", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
