# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmod(RPackage):
	"""Dynamic Modeling and Parameter Estimation in ODE Models

	The framework provides functions to generate ODEs of reaction
    networks, parameter transformations, observation functions, residual functions,
    etc. The framework follows the paradigm that derivative information should be
    used for optimization whenever possible. Therefore, all major functions produce
    and can handle expressions for symbolic derivatives. The methods used in dMod
    were published in Kaschek et al, 2019, <doi:10.18637/jss.v088.i10>.
	"""
	
	cran = "dMod" 

	version("1.0.2", md5="6eaf703295a926f5898845c011e84bc1")

	depends_on("r-code@1:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
