# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmcp(RPackage):
	"""Graph Based Multiple Comparison Procedures

	Functions and a graphical user interface for graphical described
    multiple test procedures.
	"""
	
	homepage = "https://github.com/kornl/gMCP"
	cran = "gMCP" 

	version("0.8-17", md5="00f9c2c8e9b039a7f16ab35c58efe6a4")
	version("0.8-16", md5="ad150929e7932c515fae1c64d56334b5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-polynomf", type=("build", "run"))
	depends_on("r-multcomp@1.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-commonjavajars@1.1:", type=("build", "run"))
	depends_on("r-rjava@0.6.3:", type=("build", "run"))
	depends_on("r-javagd", type=("build", "run"))
	depends_on("r-xlsxjars@0.6.1:", type=("build", "run"))
	depends_on("openjdk@5:", type=("build", "link", "run"))
