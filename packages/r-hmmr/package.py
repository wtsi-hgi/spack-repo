# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmmr(RPackage):
	""""Mixture and Hidden Markov Models with R" Datasets and Example
Code

	Datasets and code examples that accompany our book Visser & Speekenbrink (2021), "Mixture and Hidden Markov Models with R", <https://depmix.github.io/hmmr/>.
	"""
	
	homepage = "<https://depmix.github.io/hmmr/>"
	cran = "hmmr" 

	version("1.0-0", md5="82a46e20d5000a249073f8a4b9ac4c37")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-depmixs4", type=("build", "run"))
