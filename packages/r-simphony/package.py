# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimphony(RPackage):
	"""Simulating Large-Scale, Rhythmic Data

	A tool for simulating rhythmic data: transcriptome data using
  Gaussian or negative binomial distributions, and behavioral activity data
  using Bernoulli or Poisson distributions. See Singer et al. (2019)
  <doi:10.7717/peerj.6985>.
	"""
	
	homepage = "https://simphony.hugheylab.org"
	cran = "simphony" 

	version("1.0.3", md5="b685ad24ddb96ee3c213d88dcda340aa")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-data-table@1.11.4:", type=("build", "run"))
	depends_on("r-foreach@1.4.4:", type=("build", "run"))
