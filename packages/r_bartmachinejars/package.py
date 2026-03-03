# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBartmachinejars(RPackage):
	"""bartMachine JARs

	These are bartMachine's Java dependency libraries. Note: this package has no functionality of its own and should not be installed as a standalone package without bartMachine.
	"""
	
	cran = "bartMachineJARs" 

	version("1.2.1", md5="3620f905ec49920e7c9bc56a56ab834e")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-rjava@0.9.8:", type=("build", "run"))
	depends_on("openjdk@1.8:", type=("build", "link", "run"))
