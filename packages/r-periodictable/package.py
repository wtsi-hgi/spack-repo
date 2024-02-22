# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeriodictable(RPackage):
	"""Periodic Table of the Elements

	Provides a dataset containing properties for chemical elements.
    Helper functions are also provided to access some atomic properties.
	"""
	
	cran = "PeriodicTable" 

	version("0.1.2", md5="839c3e54aa6902ca6a283def2f1b520c")

	depends_on("r@3.3.1:", type=("build", "run"))
