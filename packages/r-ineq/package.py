# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIneq(RPackage):
	"""Measuring Inequality, Concentration, and Poverty

	Inequality, concentration, and poverty measures. Lorenz curves (empirical and theoretical).
	"""
	
	cran = "ineq" 

	version("0.2-13", md5="e2561a25905ac60168c18bb4f6c1b253")

	depends_on("r@2.10:", type=("build", "run"))
