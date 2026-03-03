# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnmpa(RPackage):
	"""Ecological Niche Modeling using Presence-Absence Data

	A set of tools to perform Ecological Niche Modeling with
    presence-absence data. It includes algorithms for data partitioning, 
    model fitting, calibration, evaluation, selection, and prediction. 
    Other functions help to explore signals of ecological niche using univariate
    and multivariate analyses, and model features such as variable response 
    curves and variable importance. Unique characteristics of this package are
    the ability to exclude models with concave quadratic responses, and the
    option to clamp model predictions to specific variables. These tools are
    implemented following principles proposed in
    Cobos et al., (2022) <doi:10.17161/bi.v17i.15985>, 
    Cobos et al., (2019) <doi:10.7717/peerj.6281>, 
    and Peterson et al., (2008) <doi:10.1016/j.ecolmodel.2007.11.008>.
	"""
	
	homepage = "https://github.com/Luisagi/enmpa"
	cran = "enmpa" 

	version("0.1.5", md5="752d8e82e66a23fbca7409ec31de6e29")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-snow", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
