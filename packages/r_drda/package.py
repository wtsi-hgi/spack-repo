# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrda(RPackage):
	"""Dose-Response Data Analysis

	Fit logistic functions to observed dose-response continuous
    data and evaluate goodness-of-fit measures. See Malyutina A., Tang J.,
    and Pessia A. (2023) <doi:10.18637/jss.v106.i04>.
	"""
	
	homepage = "https://github.com/albertopessia/drda"
	cran = "drda" 

	version("2.0.3", md5="4d97a81cb3231adaf3cd9a933fba255e")

	depends_on("r@3.6:", type=("build", "run"))
