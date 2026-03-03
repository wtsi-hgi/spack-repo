# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REncompasstest(RPackage):
	"""Direct Multi-Step Forecast Based Comparison of Nested Models via
an Encompassing Test

	The encompassing test is developed based on multi-step-ahead predictions of two nested models as in Pitarakis, J. (2023) <doi:10.48550/arXiv.2312.16099>. The statistics are standardised to a normal distribution, and the null hypothesis is that the larger model contains no additional useful information. P-values will be provided in the output.
	"""
	
	cran = "EncompassTest" 

	version("0.22", md5="b53d0d4a93f727a0849bad1e446cfd1d")

	depends_on("r-pracma", type=("build", "run"))
