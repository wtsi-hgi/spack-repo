# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsolde(RPackage):
	"""Integrative Statistics of alleLe Dependent Expression

	This package provides ISoLDE a new method for identifying imprinted genes. This method is dedicated to data arising from RNA sequencing technologies. The ISoLDE package implements original statistical methodology described in the publication below.
	"""
	
	homepage = "www.r-project.org"
	bioc = "ISoLDE"

	version("1.36.0", commit="c33af43eb7b7542ddb6e8ba1422e8bb22883b370")
	version("1.30.0", commit="e59ef5ecd4ad8750da080f0bb242647cade3f463")

	depends_on("r@3.3:", type=("build", "run"))
