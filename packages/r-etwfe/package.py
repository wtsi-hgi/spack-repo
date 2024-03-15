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

	version("0.4.0", md5="d14daf85f007a6ad59fd285991568f07")

	depends_on("r-fixest@0.11.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-marginaleffects@0.10:", type=("build", "run"))
