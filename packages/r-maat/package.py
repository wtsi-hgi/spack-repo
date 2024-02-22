# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaat(RPackage):
	"""Multiple Administrations Adaptive Testing

	Provides an extension of the shadow-test approach to computerized adaptive
    testing (CAT) implemented in the 'TestDesign' package for the assessment framework
    involving multiple tests administered periodically throughout the year. This framework
    is referred to as the Multiple Administrations Adaptive Testing (MAAT) and supports
    multiple item pools vertically scaled and multiple phases (stages) of CAT within each test.
    Between phases and tests, transitioning from one item pool (and associated constraints)
    to another is allowed as deemed necessary to enhance the quality of measurement.
	"""
	
	homepage = "https://choi-phd.github.io/maat/"
	cran = "maat" 

	version("1.1.0", md5="472a4d78269beac1c76cb98f017be82c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-testdesign@1.3.3:", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-diagram", type=("build", "run"))
