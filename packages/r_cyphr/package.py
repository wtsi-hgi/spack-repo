# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCyphr(RPackage):
	"""High Level Encryption Wrappers

	Encryption wrappers, using low-level support from
    'sodium' and 'openssl'.  'cyphr' tries to smooth over some pain
    points when using encryption within applications and data analysis
    by wrapping around differences in function names and arguments in
    different encryption providing packages.  It also provides
    high-level wrappers for input/output functions for seamlessly
    adding encryption to existing analyses.
	"""
	
	homepage = "https://github.com/ropensci/cyphr"
	cran = "cyphr" 

	version("1.1.4", md5="6119be52ddef8cec6eb5ade388fd3ede")

	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-openssl@0.9.9:", type=("build", "run"))
	depends_on("r-sodium@1.2.1:", type=("build", "run"))
