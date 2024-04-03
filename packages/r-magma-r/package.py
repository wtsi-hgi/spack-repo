# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMagmaR(RPackage):
	"""MAny-Group MAtching

	Balancing quasi-experimental field research for effects of covariates is fundamental for drawing causal inference. Propensity Score Matching deals with this issue but current
    techniques are restricted to binary treatment variables. Moreover, they provide several solutions without providing a comprehensive framework on choosing the best model. The
    'MAGMA.R' -package addresses these restrictions by offering nearest neighbor matching for two to four groups. It also includes the option to match data of a 2x2 design. In addition, 
    'MAGMA.R' includes a framework for evaluating the post-matching balance. The package includes functions for the matching process and matching reporting. We provide a tutorial on 
    'MAGMA.R' as vignette. More information on 'MAGMA.R' can be found in Feuchter, M. D., Urban, J., Scherrer V., Breit, M. L., and Preckel F. (2022) <https://osf.io/p47nc/>.
	"""
	
	cran = "MAGMA.R" 

	version("1.0.1", md5="6889fc60d58ba95dcb6b5747e3c590e6")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-tidyverse@2:", type=("build", "run"))
	depends_on("r-doparallel@1.0.17:", type=("build", "run"))
	depends_on("r-foreach@1.5.2:", type=("build", "run"))
	depends_on("r-metafor@4.4.0:", type=("build", "run"))
	depends_on("r-robumeta@2.1:", type=("build", "run"))
	depends_on("r-psych@2.3.9:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.4:", type=("build", "run"))
	depends_on("r-janitor@2.2:", type=("build", "run"))
	depends_on("r-flextable@0.9.4:", type=("build", "run"))
	depends_on("r-overlapping@2.1:", type=("build", "run"))
	depends_on("r-purrr@1.0.1:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.4:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
