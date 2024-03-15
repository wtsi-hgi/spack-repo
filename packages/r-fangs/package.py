# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFangs(RPackage):
	"""Feature Allocation Neighborhood Greedy Search Algorithm

	A neighborhood-based, greedy search algorithm is performed to estimate a feature allocation by minimizing the expected loss based on posterior samples from the feature allocation distribution. The method is currently under peer review but an earlier draft is available in Dahl, Johnson, and Andros (2022+) <doi:10.48550/arXiv.2207.13824>.
	"""
	
	homepage = "https://github.com/dbdahl/fangs"
	cran = "fangs" 

	version("0.2.13", md5="65885038704f1aa61672560844008dd7")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("rust", type=("build", "link", "run"))
