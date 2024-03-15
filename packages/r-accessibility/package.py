# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAccessibility(RPackage):
	"""Transport Accessibility Measures

	A set of fast and convenient functions to help conducting
    accessibility analyses. Given a pre-computed travel cost matrix and a
    land use dataset (containing the location of jobs, healthcare and
    population, for example), the package allows one to calculate
    accessibility levels and accessibility poverty and inequality. The
    package covers the majority of the most commonly used accessibility
    measures (such as cumulative opportunities, gravity-based and floating
    catchment areas methods), as well as the most frequently used
    inequality and poverty metrics (such as the Palma ratio, the
    concentration and Theil indices and the FGT family of measures).
	"""
	
	homepage = "https://github.com/ipeaGIT/accessibility"
	cran = "accessibility" 

	version("1.4.0", md5="ffb83717d16c6a17a59cb863301590f4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
