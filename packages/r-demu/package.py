# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDemu(RPackage):
	"""Optimal Design Emulators via Point Processes

	Implements the Determinantal point process (DPP) based optimal design
    emulator described in Pratola, Lin and Craigmile (2018) <arXiv:1804.02089> for
    Gaussian process regression models.  See <http://www.matthewpratola.com/software>
    for more information and examples.
	"""
	
	cran = "demu" 

	version("0.3.0", md5="4cd2972376b123ab35b084b4b915a471")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-clusterr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
