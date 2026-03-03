# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlsjunkgen(RPackage):
	"""Use the MLS Junk Generator Algorithm to Generate a Stream of
Pseudo-Random Numbers

	Generate a stream of pseudo-random numbers generated using the MLS 
    Junk Generator algorithm. Functions exist to generate single pseudo-random 
    numbers as well as a vector, data frame, or matrix of pseudo-random numbers.
	"""
	
	homepage = "https://stevemyles.site/mlsjunkgen/"
	cran = "mlsjunkgen" 

	version("0.1.2", md5="49608b588f94e854d99f0027aa2e8558")

	depends_on("r@3.1.3:", type=("build", "run"))
