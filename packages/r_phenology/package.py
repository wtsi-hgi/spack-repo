# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenology(RPackage):
	"""Tools to Manage a Parametric Function that Describes Phenology
and More

	Functions used to fit and test the phenology of species based on counts. Based on Girondot, M. (2010) <doi:10.3354/esr00292> for the phenology function, Girondot, M. (2017) <doi:10.1016/j.ecolind.2017.05.063> for the convolution of negative binomial, Girondot, M. and Rizzo, A. (2015) <doi:10.2993/etbi-35-02-337-353.1> for Bayesian estimate, Pfaller JB, ..., Girondot M (2019) <doi:10.1007/s00227-019-3545-x> for tag-loss estimate, Hancock J, ..., Girondot M (2019) <doi:10.1016/j.ecolmodel.2019.04.013> for nesting history, Laloe J-O, ..., Girondot M, Hays GC (2020) <doi:10.1007/s00227-020-03686-x> for aggregating several seasons.
	"""
	
	cran = "phenology" 

	version("9.1", md5="de9f3a54f212073b653f41f4a01b79bc")

	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-helpersmg@6.0.1:", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
