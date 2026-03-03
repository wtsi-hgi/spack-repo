# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixdir(RPackage):
	"""Cluster High Dimensional Categorical Datasets

	Scalable Bayesian clustering of categorical datasets. The package implements a hierarchical Dirichlet 
    (Process) mixture  of multinomial distributions. It is thus a probabilistic latent class model (LCM) and can be used
    to reduce the  dimensionality of hierarchical data and cluster individuals into latent classes. It can automatically
    infer an appropriate number of latent classes or find k classes, as defined by the user.  The model is based on a
    paper by Dunson and Xing (2009) <doi:10.1198/jasa.2009.tm08439>, but implements a scalable variational inference algorithm so that it is
    applicable to large datasets. It is described and tested in the accompanying paper by 
    Ahlmann-Eltze and Yau (2018) <doi:10.1109/DSAA.2018.00068>.
	"""
	
	homepage = "https://github.com/const-ae/mixdir"
	cran = "mixdir" 

	version("0.3.0", md5="f014dd4705d03c57afbb9ba0f0663459")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
