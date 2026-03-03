# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlis(RPackage):
	"""Multiplicity Control using Pooled LIS Statistic

	A multiple testing procedure for testing several groups of 
        hypotheses is implemented. Linear dependency among the hypotheses 
        within the same group is modeled by using hidden Markov Models. 
        It is noted that a smaller p value does not necessarily imply 
        more significance due to the dependency. A typical application is 
        to analyze genome wide association studies datasets, where SNPs 
        from the same chromosome are treated as a group and exhibit 
        strong linear genomic dependency. See Wei Z, Sun W, Wang K, 
        Hakonarson H (2009) <doi:10.1093/bioinformatics/btp476> for more details.
	"""
	
	cran = "PLIS" 

	version("1.2", md5="1bc61f76529cf7ca7e35089489a3a9ce")

