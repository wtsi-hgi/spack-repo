# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFormulops(RPackage):
	"""Mathematical Operations on R Formula

	Perform mathematical operations on R formula (add, subtract, multiply, etc.) and substitute parts of formula.
	"""
	
	homepage = "https://github.com/billdenney/formulops"
	cran = "formulops" 

	version("0.5.0", md5="74514a5a831051fa578b9b1166ec70fc")

	depends_on("r@3.5:", type=("build", "run"))
