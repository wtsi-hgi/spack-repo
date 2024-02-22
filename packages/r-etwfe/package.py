# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REtwfe(RPackage):
	"""Extended Two-Way Fixed Effects

	Convenience functions for implementing extended two-way 
  fixed effect regressions a la Wooldridge (2021, 2022)
  <doi:10.2139/ssrn.3906345>, <doi:10.2139/ssrn.4183726>.
	"""
	
	homepage = "https://grantmcdermott.com/etwfe/"
	cran = "etwfe" 

	version("0.3.5", md5="fc09d20fb4ca9e2cd09b075e634fcf47")

	depends_on("r-fixest@0.11.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-marginaleffects@0.10:", type=("build", "run"))
