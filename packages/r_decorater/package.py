# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecorater(RPackage):
	"""Fit and Deploy DECORATE Trees

	DECORATE (Diverse Ensemble Creation by Oppositional Relabeling
    of Artificial Training Examples) builds an ensemble of J48 trees by recursively
    adding artificial samples of the training data ("Melville, P., & Mooney, R. J. (2005) <DOI:10.1016/j.inffus.2004.04.001>").
	"""
	
	cran = "DecorateR" 

	version("0.1.2", md5="11e2c6a44ff8fc8feea62d4f80ff56dd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rweka", type=("build", "run"))
	depends_on("r-rwekajars", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
