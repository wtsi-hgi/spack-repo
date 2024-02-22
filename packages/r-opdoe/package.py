# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpdoe(RPackage):
	"""Optimal Design of Experiments

	Several function related to Experimental Design are implemented here, see
  "Optimal Experimental Design with R" by Rasch D. et. al (ISBN 9781439816974).
	"""
	
	cran = "OPDOE" 

	version("1.0-10", md5="c963c1dafeb929959db45564ae7ecb79")

	depends_on("r-gmp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-crossdes", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
