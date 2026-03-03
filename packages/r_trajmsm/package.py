# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrajmsm(RPackage):
	"""Marginal Structural Models with Latent Class Growth Analysis of
Treatment Trajectories

	Implements marginal structural models combined with a latent class growth analysis framework for assessing the causal effect of treatment trajectories. Based on the approach described in "Marginal Structural Models with Latent Class Growth Analysis of Treatment Trajectories" Diop, A., Sirois, C., Guertin, J.R., Schnitzer, M.E., Candas, B., Cossette, B., Poirier, P., Brophy, J., Mésidor, M., Blais, C. and Hamel, D., (2023) <doi:10.1177/09622802231202384>. 
	"""
	
	homepage = "https://github.com/awamaeva/R-package-trajmsm"
	cran = "trajmsm" 

	version("0.1.0", md5="c8c41fff7b20789aa018d4d25dbbc10a")

	depends_on("r-class", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-flexmix", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
