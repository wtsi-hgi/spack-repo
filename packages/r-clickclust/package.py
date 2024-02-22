# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClickclust(RPackage):
	"""Model-Based Clustering of Categorical Sequences

	Clustering categorical sequences by means of finite mixtures with Markov model components is the main utility of ClickClust. The package also allows detecting blocks of equivalent states by forward and backward state selection procedures.
	"""
	
	cran = "ClickClust" 

	version("1.1.6", md5="12e514ebbe1d3d9a259a03098730a49c")

	depends_on("r@3:", type=("build", "run"))
