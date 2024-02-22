# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelect(RPackage):
	"""Determines Species Probabilities Based on Functional Traits

	The objective of these functions is to derive a species assemblage
    that satisfies a functional trait profile. Restoring resilient ecosystems
    requires a flexible framework for selecting assemblages that are based on the
    functional traits of species. However, current trait-based models have been
    limited to algorithms that can only select species by optimising specific trait
    values, and could not elegantly accommodate the common desire among restoration
    ecologists to produce functionally diverse assemblages. We have solved this
    problem by applying a non-linear optimisation algorithm that optimises Rao Q,
    a closed-form functional trait diversity index that incorporates species
    abundances, subject to other linear constraints. This framework generalises
    previous models that only optimised the entropy of the community, and can
    optimise both functional diversity and entropy simultaneously. This package
    can also be used to generate experimental assemblages to test the effects
    of community-level traits on community dynamics and ecosystem function. The
    method is based on theory discussed in Laughlin (2014, Ecology Letters)
    <doi.org/10.1111/ele.12288>.
	"""
	
	cran = "Select" 

	version("1.4", md5="6d88d131c4033118a831e6fb67c964d8")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-fd", type=("build", "run"))
