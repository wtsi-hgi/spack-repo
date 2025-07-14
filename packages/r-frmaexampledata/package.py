# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrmaexampledata(RPackage):
	"""Frma Example Data

	Data files used by the examples in frma and frmaTools packages
	"""
	
	bioc = "frmaExampleData"

	version("1.44.0", commit="aefb4d929a9d08e52d92b4a6d2b684af0e82b446")
	version("1.38.0", commit="5077fc6ca76f3b49ed7f0a0d89125a232d700ef9")

	depends_on("r@2.10:", type=("build", "run"))

