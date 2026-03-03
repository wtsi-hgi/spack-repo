# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnitizer(RPackage):
	"""Interactive R Unit Tests

	Simplifies regression tests by comparing objects produced by test
    code with earlier versions of those same objects.  If objects are unchanged
    the tests pass, otherwise execution stops with error details.  If in
    interactive mode, tests can be reviewed through the provided interactive
    environment.
	"""
	
	homepage = "https://github.com/brodieG/unitizer"
	cran = "unitizer" 

	version("1.4.20", md5="a0e2e77bc73d40eff1e07cd684a16e80")

	depends_on("r-crayon@1.3.2:", type=("build", "run"))
	depends_on("r-diffobj@0.1.5.9000:", type=("build", "run"))
