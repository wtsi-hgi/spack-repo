# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcceptancesampling(RPackage):
	"""Creation and Evaluation of Acceptance Sampling Plans

	Provides functionality for creating and
	evaluating acceptance sampling plans. Sampling plans can be single,
	double or multiple.
	"""
	
	homepage = "https://github.com/andreaskiermeier/AcceptanceSampling"
	cran = "AcceptanceSampling" 

	version("1.0-10", md5="cccf037fcede6abc4636d6d4cfe88d0f")

	depends_on("r@2.4:", type=("build", "run"))
