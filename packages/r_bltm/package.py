# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBltm(RPackage):
	"""Bayesian Latent Threshold Modeling

	Fits latent threshold model for simulated data
    and describes how to adjust model using real data. Implements algorithm
    proposed by Nakajima and West (2013) <doi:10.1080/07350015.2012.747847>. 
    This package has a function to generate data, a function to configure 
    priors and a function to fit the model. Examples may be checked inside 
    the demonstration files.
	"""
	
	homepage = "https://github.com/curso-r/bltm"
	cran = "bltm" 

	version("0.1.0", md5="5362a797c9f914c50008cc8fc2c41f73")

	depends_on("r-mvnfast", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
