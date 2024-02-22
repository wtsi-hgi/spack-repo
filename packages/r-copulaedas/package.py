# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopulaedas(RPackage):
	"""Estimation of Distribution Algorithms Based on Copulas

	Provides a platform where EDAs (estimation of
    distribution algorithms) based on copulas can be implemented and
    studied. The package offers complete implementations of various
    EDAs based on copulas and vines, a group of well-known
    optimization problems, and utility functions to study the
    performance of the algorithms. Newly developed EDAs can be easily
    integrated into the package by extending an S4 class with generic
    functions for their main components.
	"""
	
	homepage = "https://github.com/yasserglez/copulaedas"
	cran = "copulaedas" 

	version("1.4.3", md5="457d03d2b5bdeb195c3cac3961979fdb")

	depends_on("r-copula", type=("build", "run"))
	depends_on("r-vines", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
