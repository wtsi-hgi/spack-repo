# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBenfordtests(RPackage):
	"""Statistical Tests for Evaluating Conformity to Benford's Law

	Several specialized statistical tests and support functions 
			for determining if numerical data could conform to Benford's law.
	"""
	
	homepage = "https://cran.r-project.org/package=BenfordTests"
	cran = "BenfordTests" 

	version("1.2.0", md5="8a93a90942af387ab4951c7d6c74892e")

	depends_on("r@3:", type=("build", "run"))
