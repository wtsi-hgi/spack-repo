# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHero(RPackage):
	"""Spatio-Temporal (Hero) Sandwich Smoother

	An implementation of the sandwich smoother proposed in Fast Bivariate Penalized Splines by Xiao et al. (2012) <doi:10.1111/rssb.12007>.    A hero is a specific type of sandwich.  Dictionary.com (2018) <https://www.dictionary.com> describes a hero as: a large sandwich, usually consisting of a small loaf of bread or long roll cut in half lengthwise and containing a variety of ingredients, as meat, cheese, lettuce, and tomatoes. Also implements the spatio-temporal sandwich smoother of French and Kokoszka (2021) <doi:10.1016/j.spasta.2020.100413>.
	"""
	
	cran = "hero" 

	version("0.6", md5="0b62a0343fc8c308ffb877f463c1efe8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
