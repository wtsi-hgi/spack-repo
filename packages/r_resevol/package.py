# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResevol(RPackage):
	"""Simulate Agricultural Production and Evolution of Pesticide
Resistance

	Simulates individual-based models of agricultural pest management
    and the evolution of pesticide resistance. Management occurs on a spatially
    explicit landscape that is divided into an arbitrary number of farms that
    can grow one of up to 10 crops and apply one of up to 10 pesticides. Pest
    genomes are modelled in a way that allows for any number of pest traits with
    an arbitrary covariance structure that is constructed using an evolutionary
    algorithm in the mine_gmatrix() function. Simulations are then run using the
    run_farm_sim() function. This package thereby allows for highly mechanistic
    social-ecological models of the evolution of pesticide resistance under
    different types of crop rotation and pesticide application regimes.
	"""
	
	homepage = "https://bradduthie.github.io/resevol/"
	cran = "resevol" 

	version("0.3.4.0", md5="ffa9b23621eeb0bd09104e26660f5516")

	depends_on("r@4:", type=("build", "run"))
