# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsdistr(RPackage):
	"""Distributions Derived from Normal Distribution

	Presentation of distributions such as: two-piece power normal (TPPN), plasticizing component (PC), DS normal (DSN), expnormal (EN), Sulewski plasticizing component (SPC), easily changeable kurtosis (ECK) distributions. Density, distribution function, quantile function and random generation are presented. For details on this method see: Sulewski (2019) <doi:10.1080/03610926.2019.1674871>, Sulewski (2021) <doi:10.1080/03610926.2020.1837881>, Sulewski (2021) <doi:10.1134/S1995080221120337>, Sulewski (2022) <"New members of the Johnson family of probability dis-tributions: properties and application">, Sulewski, Volodin (2022) <doi:10.1134/S1995080222110270>, Sulewski (2023) <doi:10.17713/ajs.v52i3.1434>.
	"""
	
	cran = "PSDistr" 

	version("0.0.1", md5="cfc1156463d349151282e9f6c5721dd2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
