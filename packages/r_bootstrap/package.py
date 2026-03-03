# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootstrap(RPackage):
	"""Functions for the Book "An Introduction to the Bootstrap"

	Software (bootstrap, cross-validation, jackknife) and data
        for the book "An Introduction to the Bootstrap" by B. Efron and
        R. Tibshirani, 1993, Chapman and Hall. This package is
        primarily provided for projects already based on it, and for
        support of the book. New projects should preferentially use the
        recommended package "boot".
	"""
	
	homepage = "https://gitlab.com/scottkosty/bootstrap"
	cran = "bootstrap" 

	version("2019.6", md5="d794b81b1e07ef2f214e58c7b4c0ba4f")

	depends_on("r@2.10:", type=("build", "run"))
