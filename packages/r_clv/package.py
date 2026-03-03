# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClv(RPackage):
	"""Cluster Validation Techniques

	Package contains most of the popular internal and external
        cluster validation methods ready to use for the most of the
        outputs produced by functions coming from package "cluster".
        Package contains also functions and examples of usage for
        cluster stability approach that might be applied to algorithms
        implemented in "cluster" package as well as user defined
        clustering algorithms.
	"""
	
	cran = "clv" 

	version("0.3-2.4", md5="bad3bb2af579830b283b0d8b5fa58a6f")

	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
