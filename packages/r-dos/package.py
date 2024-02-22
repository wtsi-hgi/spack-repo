# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDos(RPackage):
	"""Design of Observational Studies

	Contains data sets, examples and software from the book Design of Observational Studies by Paul R. Rosenbaum, New York: Springer, <doi:10.1007/978-1-4419-1213-8>, ISBN 978-1-4419-1212-1.
	"""
	
	cran = "DOS" 

	version("1.0.0", md5="415329e7bb68a4f3bc08a4eedacad2c1")

	depends_on("r-mass", type=("build", "run"))
