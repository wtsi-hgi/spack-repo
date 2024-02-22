# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHowmanyimputations(RPackage):
	"""Calculate How many Imputations are Needed for Multiple
Imputation

	When performing multiple imputations, while 5-10 imputations are
             sufficient for obtaining point estimates, a larger number of
             imputations are needed for proper standard error estimates.
             This package allows you to calculate how many imputations are
             needed, following the work of von Hippel (2020)
             <doi:10.1177/0049124117747303>.
	"""
	
	homepage = "https://errickson.net/howManyImputations/"
	cran = "howManyImputations" 

	version("0.2.4", md5="82f07f6b1cf72df98fee0f999b4fd417")

	depends_on("r-mice", type=("build", "run"))
