# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXegadfgene(RPackage):
	"""Gene Operations for Real-Coded Genes

	Representation-dependent gene level operations  
        for genetic and evolutionary algorithms with real-coded genes
        are collected in this package. The common feature of the gene
        operations is that all of them are useful for derivation-free
        optimization algorithms. At the moment the package  
        implements initialization, mutation, crossover, and replication 
        operations for differential evolution as described in
        Price, Kenneth V., Storn, Rainer M. and Lampinen, Jouni A. (2005)
        <doi:10.1007/3-540-31306-0>. 
	"""
	
	homepage = "<https://github.com/ageyerschulz/xegaDfGene>"
	cran = "xegaDfGene" 

	version("1.0.0.0", md5="4c192a95732bae180ee18980876e5f40")

	depends_on("r-xegaselectgene", type=("build", "run"))
