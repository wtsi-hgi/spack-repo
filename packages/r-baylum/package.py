# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaylum(RPackage):
	"""Chronological Bayesian Models Integrating Optically Stimulated
Luminescence and Radiocarbon Age Dating

	Bayesian analysis of luminescence data and C-14 age estimates. Bayesian models are based on the following publications: Combes, B. & Philippe, A. (2017) <doi:10.1016/j.quageo.2017.02.003> and Combes et al (2015) <doi:10.1016/j.quageo.2015.04.001>. This includes, amongst others, data import, export, application of age models and palaeodose model.
	"""
	
	homepage = "https://CRAN.r-project.org/package=BayLum"
	cran = "BayLum" 

	version("0.3.1", md5="7d7b062c40e30edbe913ac4ac8dc9d41")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-coda@0.19:", type=("build", "run"))
	depends_on("r-hexbin@1.28.3:", type=("build", "run"))
	depends_on("r-kernsmooth@2.23:", type=("build", "run"))
	depends_on("r-rjags@4.13:", type=("build", "run"))
	depends_on("r-runjags@2.2.1:", type=("build", "run"))
	depends_on("r-luminescence@0.9.21:", type=("build", "run"))
	depends_on("r-archaeophases@1.8:", type=("build", "run"))
	depends_on("jags@4.3.2:", type=("build", "link", "run"))
