# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROwea(RPackage):
	"""Optimal Weight Exchange Algorithm for Optimal Designs for Three
Models

	An implementation of optimal weight exchange algorithm Yang(2013) <doi:10.1080/01621459.2013.806268> for three models.
    They are Crossover model with subject dropout, crossover model with proportional
    first order residual effects and interference model. You can use it to find either
    A-opt or D-opt approximate designs. Exact designs can be automatically rounded
    from approximate designs and relative efficiency is provided as well.
	"""
	
	cran = "OWEA" 

	version("0.1.2", md5="a49dfe5d9fe6f5a06534aeac203b8351")

	depends_on("r-gtools@3.9.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-shiny@1.7.2:", type=("build", "run"))
