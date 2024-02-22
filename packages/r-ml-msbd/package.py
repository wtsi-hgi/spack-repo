# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlMsbd(RPackage):
	"""Maximum Likelihood Inference on Multi-State Trees

	Inference of a multi-states birth-death model from a phylogeny, comprising a number of states N, birth and death rates for each state and on which edges each state appears. Inference is done using a hybrid approach: states are progressively added in a greedy approach. For a fixed number of states N the best model is selected via maximum likelihood. Reference: J. Barido-Sottani, T. G. Vaughan and T. Stadler (2018) <doi:10.1098/rsif.2018.0512>.
	"""
	
	cran = "ML.MSBD" 

	version("1.2.1", md5="24ce84007a890c252f6f97fddeca88b6")

	depends_on("r-ape@5.1:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
