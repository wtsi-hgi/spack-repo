# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpt(RPackage):
	"""Multinomial Processing Tree Models

	Fitting and testing multinomial processing tree (MPT) models, a
  class of nonlinear models for categorical data.  The parameters are the
  link probabilities of a tree-like graph and represent the latent cognitive
  processing steps executed to arrive at observable response categories
  (Batchelder & Riefer, 1999 <doi:10.3758/bf03210812>; Erdfelder et al., 2009
  <doi:10.1027/0044-3409.217.3.108>; Riefer & Batchelder, 1988
  <doi:10.1037/0033-295x.95.3.318>).
	"""
	
	homepage = "http://www.mathpsy.uni-tuebingen.de/wickelmaier/"
	cran = "mpt" 

	version("0.8-0", md5="b84831638aec738ed816305a59ca6774")

	depends_on("r@3.5:", type=("build", "run"))
