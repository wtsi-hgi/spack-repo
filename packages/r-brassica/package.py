# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrassica(RPackage):
	"""1970s BASIC Interpreter

	Executes BASIC programs from the 1970s, for historical and
    educational purposes. This enables famous examples of early machine
    learning, artificial intelligence, natural language processing, cellular
    automata, and so on, to be run in their original form.
	"""
	
	cran = "brassica" 

	version("1.0.2", md5="71a2f0422870c82ece30183ed8382dfb")

	depends_on("r@3.3:", type=("build", "run"))
