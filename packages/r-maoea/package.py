# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaoea(RPackage):
	"""Many Objective Evolutionary Algorithm

	A set of evolutionary algorithms to solve many-objective optimization. 
    Hybridization between the algorithms are also facilitated. Available algorithms are:
    'SMS-EMOA' <doi:10.1016/j.ejor.2006.08.008>
    'NSGA-III' <doi:10.1109/TEVC.2013.2281535>
    'MO-CMA-ES' <doi:10.1145/1830483.1830573>
    The following many-objective benchmark problems are also provided: 
    'DTLZ1'-'DTLZ4' from Deb, et al. (2001) <doi:10.1007/1-84628-137-7_6> and
    'WFG4'-'WFG9' from Huband, et al. (2005) <doi:10.1109/TEVC.2005.861417>.
	"""
	
	homepage = "https://github.com/dots26/MaOEA"
	cran = "MaOEA" 

	version("0.6.2", md5="8399e2598bc9bece1df2cbc4b78c2c18")

	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-nsga2r", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("python@3:", type=("build", "link", "run"))
	depends_on("py-numpy", type=("build", "link", "run"))
	depends_on("py-cloudpickle", type=("build", "link", "run"))
