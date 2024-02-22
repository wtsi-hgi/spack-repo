# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBmscstan(RPackage):
	"""Bayesian Multilevel Single Case Models using 'Stan'

	Analyse single case analyses against a control group.
    Its purpose is to provide a flexible, with good power and
    low first type error
    approach that can manage at the same time controls' and patient's data.
    The use of Bayesian statistics allows to test both the alternative and
    null hypothesis.
    Scandola, M., & Romano, D. (2020, August 3). <doi:10.31234/osf.io/sajdq>
    Scandola, M., & Romano, D. (2021). <doi:10.1016/j.neuropsychologia.2021.107834>.
	"""
	
	homepage = "https://github.com/michelescandola/bmscstan"
	cran = "bmscstan" 

	version("1.2.1.0", md5="54b4461cb55f19553df7709eaaffbfcb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-logspline", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
