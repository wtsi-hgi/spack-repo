# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REase(RPackage):
	"""Simulating Explicit Population Genetics Models

	Implementation in a simple and efficient way of fully customisable population genetics simulations,
    considering multiple loci that have epistatic interactions. Specifically suited to the modelling of
    multilocus nucleocytoplasmic systems (with both diploid and haploid loci), it is nevertheless possible
    to simulate purely diploid (or purely haploid) genetic models.
	Examples of models that can be simulated with Ease are numerous, for example models of genetic
	incompatibilities as presented by Marie-Orleach et al. (2022) <doi:10.1101/2022.07.25.501356>.
	Many others are conceivable, although few are actually explored, Ease having been developed
	in particular to provide a solution so that these kinds of models can be simulated simply.
	"""
	
	cran = "Ease" 

	version("0.1.2", md5="c3e7cc4b39a447aec18a05bbc0524fd7")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
