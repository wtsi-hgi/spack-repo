# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegent(RPackage):
	"""Risk Estimation for Genetic and Environmental Traits

	Produces population distribution of disease risk and statistical risk categories, and predicts risks for individuals with genotype information.
	"""
	
	cran = "REGENT" 

	version("1.0.6", md5="2cb43d1d4b6c5eded1d7668bd66beee7")

	depends_on("r@2.14:", type=("build", "run"))
