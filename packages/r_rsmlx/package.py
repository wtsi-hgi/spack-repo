# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsmlx(RPackage):
	"""R Speaks 'Monolix'

	Provides methods for model building and model evaluation of mixed effects models using 
    'Monolix' <https://monolix.lixoft.com>. 'Monolix' is a software tool for nonlinear mixed effects 
    modeling that must have been installed in order to use 'Rsmlx'. 
    Among other tasks, 'Rsmlx' provides a powerful tool for automatic PK model building, performs 
    statistical tests for model assessment, bootstrap simulation and likelihood profiling for 
    computing confidence intervals. 'Rsmlx' also proposes several automatic covariate search methods for 
    mixed effects models. 
	"""
	
	homepage = "https://monolix.lixoft.com/rsmlx/"
	cran = "Rsmlx" 

	version("2023.1.5", md5="3dceedea84e5b56e8bc6e961cf490c72")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
