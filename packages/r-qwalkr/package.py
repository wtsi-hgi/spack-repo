# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQwalkr(RPackage):
	"""Handle Continuous-Time Quantum Walks with R

	Functions and tools for creating, visualizing, and investigating properties of continuous-time quantum walks, including efficient calculation of matrices such as the mixing matrix, average mixing matrix, and spectral decomposition of the Hamiltonian. E. Farhi (1997): <arXiv:quant-ph/9706062v2>; C. Godsil (2011) <arXiv:1103.2578v3>.
	"""
	
	homepage = "https://github.com/vitormarquesr/qwalkr"
	cran = "qwalkr" 

	version("0.1.0", md5="6756cfd9c4a9b472180469f4edd43bcc")

	depends_on("r-lifecycle", type=("build", "run"))
