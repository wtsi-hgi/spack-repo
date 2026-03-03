# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfd(RPackage):
	"""Space-Filling Design Library

	
    A collection of pre-optimized space-filling designs, for up to ten 
    parameters, is contained here. Functions are provided to access designs 
    described by Husslage et al (2011) <doi:10.1007/s11081-010-9129-8> and
    Wang and Fang (2005) <doi:10.1142/9789812701190_0040>. The design types 
    included are Audze-Eglais, MaxiMin, and uniform.
	"""
	
	cran = "sfd" 

	version("0.1.0", md5="d78672808db82a9013f40bc11237cc3e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
