# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnamf(RPackage):
	"""Recursive Non-Additive Emulator for Multi-Fidelity Data

	Performs RNA emulation and active learning proposed by Heo and Sung (2023+) <arXiv:2309.11772> for multi-fidelity computer experiments. The RNA emulator is particularly useful when the simulations with different fidelity level are nonlinearly correlated. The hyperparameters in the model are estimated by maximum likelihood estimation. 
	"""
	
	cran = "RNAmf" 

	version("0.1.2", md5="b5e516dd84b6bb256e24658e4ccd83ba")

	depends_on("r-plgp", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
