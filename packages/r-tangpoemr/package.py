# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTangpoemr(RPackage):
	"""Write Chinese Tang Poems

	Write Chinese Tang Poems automatically.
	"""
	
	cran = "TangPoemR" 

	version("0.1.0", md5="fc4fbf1b80df64f65bd0683d02b97afb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-jiebar", type=("build", "run"))
