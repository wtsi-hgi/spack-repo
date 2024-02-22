# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXegagagene(RPackage):
	"""Binary Gene Operations for Genetic Algorithms

	Representation-dependent gene level operations of a 
        genetic algorithm with binary coded genes:
        Initialization of random binary genes, several gene maps for 
        binary genes, several mutation operators, several crossover
        operators with 1 and 2 kids, replication 
        pipelines for 1 and 2 kids, and, last but not least, function 
        factories for configuration. 
        See Goldberg, D. E. (1989, ISBN:0-201-15767-5).
        For crossover operators, see 
        Syswerda, G. (1989, ISBN:1-55860-066-3),
        Spears, W. and De Jong, K. (1991, ISBN:1-55860-208-9).
        For mutation operators, see 
        Stanhope, S. A. and Daida, J. M. (1996, ISBN:0-18-201-031-7).
	"""
	
	homepage = "<https://github.com/ageyerschulz/xegaGaGene>"
	cran = "xegaGaGene" 

	version("1.0.0.1", md5="9d20962adc9b20f163f1b64200f34ace")

	depends_on("r-xegaselectgene", type=("build", "run"))
