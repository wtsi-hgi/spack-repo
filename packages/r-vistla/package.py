# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVistla(RPackage):
	"""Detecting Influence Paths with Information Theory

	Traces information spread through interactions between features, utilising information theory measures and a higher-order generalisation of the concept of widest paths in graphs.
  In particular, 'vistla' can be used to better understand the results of high-throughput biomedical experiments, by organising the effects of the investigated intervention in a tree-like hierarchy from direct to indirect ones, following the plausible information relay circuits.
  Due to its higher-order nature, 'vistla' can handle multi-modality and assign multiple roles to a single feature.
	"""
	
	cran = "vistla" 

	version("2.0.1", md5="63f830f14529887bee23f23411a15120")

	depends_on("r@3.5:", type=("build", "run"))
