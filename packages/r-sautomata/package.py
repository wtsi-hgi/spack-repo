# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSautomata(RPackage):
	"""Inference and Learning in Stochastic Automata

	Machine learning provides algorithms that can learn from data and make inferences or predictions. Stochastic automata is a class of input/output devices which can model components. This work provides implementation an inference algorithm for stochastic automata which is similar to the Viterbi algorithm. Moreover, we specify a learning algorithm using the expectation-maximization technique and provide a more efficient implementation of the Baum-Welch algorithm for stochastic automata. This work is based on Inference and learning in stochastic automata was by Karl-Heinz Zimmermann(2017) <doi:10.12732/ijpam.v115i3.15>.
	"""
	
	cran = "SAutomata" 

	version("0.1.0", md5="5f6e12f917ad4bfed8c8bd1d8c531ef1")

	depends_on("r@2:", type=("build", "run"))
