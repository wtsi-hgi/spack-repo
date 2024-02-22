# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStacking(RPackage):
	"""Building Predictive Models with Stacking

	Building predictive models with stacking which is a type of ensemble learning. Learners can be specified from those implemented in 'caret'. For more information of the package, see Nukui and Onogi (2023) <doi:10.1101/2023.06.06.543970>.
	"""
	
	cran = "stacking" 

	version("0.1.2", md5="06ea323d99f8cf1d8b2d9c535fa50d1b")

	depends_on("r-caret", type=("build", "run"))
