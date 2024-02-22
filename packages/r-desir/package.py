# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesir(RPackage):
	"""Desirability Functions for Ranking, Selecting, and Integrating
Data

	Functions for (1) ranking, selecting, and prioritising  genes,
    proteins, and metabolites from high dimensional biology experiments, (2)
    multivariate hit calling in high content screens, and (3) combining data
    from diverse sources.
	"""
	
	homepage = "https://github.com/stanlazic/desiR"
	cran = "desiR" 

	version("1.2.2", md5="a49b243a7ee44e0d4e3fb5e36d91b27e")

	depends_on("r@2.10:", type=("build", "run"))
