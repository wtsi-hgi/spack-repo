# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowerpls(RPackage):
	"""Power Analysis for PLS Classification

	It estimates power and sample size for Partial Least Squares-based methods described in Andreella, et al., (2024) <arXiv:2403.10289>.
	"""
	
	homepage = "https://github.com/angeella/powerPLS"
	cran = "powerPLS" 

	version("0.1.0", md5="abb1edc8518dd7913e345c56a3ce0543")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-compositions", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-simukde", type=("build", "run"))
	depends_on("r-nipals", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
