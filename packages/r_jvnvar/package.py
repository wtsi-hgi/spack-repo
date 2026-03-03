# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJvnvar(RPackage):
	"""Value at Risk

	Many method to compute, predict and back-test VaR. For more detail, see the report: Value at Risk <researchgate.net>.
	"""
	
	cran = "jvnVaR" 

	version("1.0", md5="0da83c0bb62a57e84e17ecdda5048a1f")

	depends_on("r@2.10:", type=("build", "run"))
