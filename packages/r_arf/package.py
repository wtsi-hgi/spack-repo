# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArf(RPackage):
	"""Adversarial Random Forests

	Adversarial random forests (ARFs) recursively partition data into 
    fully factorized leaves, where features are jointly independent. The 
    procedure is iterative, with alternating rounds of generation and 
    discrimination. Data becomes increasingly realistic at each round, until 
    original and synthetic samples can no longer be reliably distinguished. 
    This is useful for several unsupervised learning tasks, such as density
    estimation and data synthesis. Methods for both are implemented in this
    package. ARFs naturally handle unstructured data with mixed continuous and 
    categorical covariates. They inherit many of the benefits of random forests, 
    including speed, flexibility, and solid performance with default parameters. 
    For details, see Watson et al. (2022) <arXiv:2205.09435>.
	"""
	
	homepage = "https://github.com/bips-hb/arf"
	cran = "arf" 

	version("0.2.0", md5="3c16755cb1dee9df8c5eda3a6876674f")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
