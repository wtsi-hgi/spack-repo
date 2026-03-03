# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXegagegene(RPackage):
	"""Grammatical Evolution

	Grammatical evolution  (see O'Neil, M. and 
        Ryan, C.  (2003,ISBN:1-4020-7444-1)) uses decoders to 
        convert linear (binary or integer genes) into programs.  
        In addition, automatic determination of codon precision 
        with a limited rule choice bias is provided.
        For a recent survey of grammatical evolution, 
        see Ryan, C., O'Neill, M., and Collins, J. J. (2018)
        <doi:10.1007/978-3-319-78717-6>.
	"""
	
	homepage = "<https://github.com/ageyerschulz/xegaGeGene>"
	cran = "xegaGeGene" 

	version("1.0.0.0", md5="5f429d90e98bc1e8506290cf26cf402f")

	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-xegaselectgene", type=("build", "run"))
	depends_on("r-xegabnf", type=("build", "run"))
	depends_on("r-xegaderivationtrees", type=("build", "run"))
