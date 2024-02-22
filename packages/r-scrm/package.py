# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScrm(RPackage):
	"""Simulating the Evolution of Biological Sequences

	A coalescent simulator that allows the rapid simulation of
    biological sequences under neutral models of evolution, see
    Staab et al. (2015) <doi:10.1093/bioinformatics/btu861>.
    Different to other coalescent based simulations,
    it has an optional approximation parameter that
    allows for high accuracy while maintaining a linear run time cost for long
    sequences. It is optimized for simulating massive data sets as produced by Next-
    Generation Sequencing technologies for up to several thousand sequences.
	"""
	
	homepage = "https://github.com/scrm/scrm-r"
	cran = "scrm" 

	version("1.7.5", md5="ebb8212bddc6abc1a7f5b7ddcf1762ee")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
