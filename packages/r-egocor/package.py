# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REgocor(RPackage):
	"""Simple Presentation of Estimated Exponential Semi-Variograms

	User friendly interface based on the R package 'gstat' to fit
    exponential parametric models to empirical semi-variograms in order to
    model the spatial correlation structure of health data. Geo-located
    health outcomes of survey participants may be used to model spatial
    effects on health in an ego-centred approach.  The package contains a
    range of functions to help explore the spatial structure of the data
    as well as visualize the fit of exponential models for various
    metaparameter combinations with respect to the number of lag intervals
    and maximal distance.  Furthermore, the outcome of interest can be
    adjusted for covariates by fitting a linear regression in a
    preliminary step before the semi-variogram fitting process.
	"""
	
	homepage = "https://github.com/julia-dyck/EgoCor"
	cran = "EgoCor" 

	version("1.1.0", md5="6e2dcdb78435763cf6b270973638a20f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gstat", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spatialtools", type=("build", "run"))
