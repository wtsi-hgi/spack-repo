# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAracneNetworks(RPackage):
	"""ARACNe-inferred gene networks from TCGA tumor datasets

	This package contains ARACNe-inferred networks from TCGA tumor datasets. It also contains a function to export them into plain-text format.
	"""
	
	bioc = "aracne.networks"

	version("1.34.0", commit="8adad99734fc829ad0c8cb26a1603772ee918429")
	version("1.28.0", commit="3c3a4fb1e3768c8b865b99ab1bae9027968a129c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-viper", type=("build", "run"))

