# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeeasy(RPackage):
	"""Solve Generalized Estimating Equations for Clustered Data

	Estimation of generalized linear models with
    correlated/clustered observations by use of generalized estimating
    equations (GEE). See e.g. Halekoh and Højsgaard, (2005,
    <doi:10.18637/jss.v015.i02>), for details. Several types of
    clustering are supported, including exchangeable variance
    structures, AR1 structures, M-dependent, user-specified variance
    structures and more. The model fitting computations are performed
    using modified code from the 'geeM' package, while the interface
    and output objects have been written to resemble the 'geepack'
    package. The package also contains additional tools for working
    with and inspecting results from the 'geepack' package, e.g. a
    'confint' method for 'geeglm' objects from 'geepack'.
	"""
	
	cran = "geeasy" 

	version("0.1.1", md5="c8e66b59c24ac3150834ddef976d3654")

	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-geem", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mess", type=("build", "run"))
