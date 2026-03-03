# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComparisonsurv(RPackage):
	"""Comparison of Survival Curves Between Two Groups

	Various statistical methods for survival analysis in comparing survival curves between two groups, including overall hypothesis tests described in Li et al. (2015) <doi:10.1371/journal.pone.0116774> and Huang et al. (2020) <doi:10.1080/03610918.2020.1753075>, fixed-point tests in Klein et al. (2007) <doi:10.1002/sim.2864>, short-term tests, and long-term tests in Logan et al. (2008) <doi:10.1111/j.1541-0420.2007.00975.x>. Some commonly used descriptive statistics and plots are also included.
	"""
	
	cran = "ComparisonSurv" 

	version("1.1.1", md5="a0dce32ffcc8dc619397f033a3e0c11c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-survrm2", type=("build", "run"))
	depends_on("r-tshrc", type=("build", "run"))
	depends_on("r-muhaz", type=("build", "run"))
