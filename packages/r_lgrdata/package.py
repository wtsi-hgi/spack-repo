# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLgrdata(RPackage):
	"""Example Datasets for a Learning Guide to R

	A largish collection of example datasets, including several classics. Many of
    these datasets are well suited for regression, classification, and visualization.
	"""
	
	cran = "lgrdata" 

	version("0.1.1", md5="7306ef5c5eff4291e25dce02403f4208")

	depends_on("r@2.10:", type=("build", "run"))
