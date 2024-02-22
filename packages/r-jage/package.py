# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJage(RPackage):
	"""Estimation of Developmental Age

	Bayesian methods for estimating developmental age from ordinal dental data. For an explanation of the model used, see Konigsberg (2015) <doi:10.3109/03014460.2015.1045430>. For details on the conditional correlation correction, see Sgheiza (2022) <doi:10.1016/j.forsciint.2021.111135>. Dental scoring is based on Moorrees, Fanning, and Hunt (1963) <doi:10.1177/00220345630420062701>.
	"""
	
	cran = "jage" 

	version("0.1.0", md5="76d42c131aceb8468bd69e42381bc937")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
