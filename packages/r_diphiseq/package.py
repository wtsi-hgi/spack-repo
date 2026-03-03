# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiphiseq(RPackage):
	"""Robust Tests for Differential Dispersion and Differential
Expression in RNA-Sequencing Data

	Implements the algorithm described in Jun Li and Alicia T. Lamere, 
    "DiPhiSeq: Robust comparison of expression levels on RNA-Seq data with large sample sizes"  (Unpublished). 
    Detects not only genes that show different 
    average expressions ("differential expression", DE), but also genes that show different 
    diversities of expressions in different groups ("differentially dispersed", DD). DD genes 
    can be important clinical markers. 'DiPhiSeq' uses a redescending penalty on the 
    quasi-likelihood function, and thus has superior robustness against outliers and other noise.
    Updates from version 0.1.0: (1) Added the option of using adaptive initial value for phi.
    (2) Added a function for estimating the proportion of outliers in the data.
    (3) Modified the input parameter names for clarity, and modified the output format for the main function.
	"""
	
	cran = "DiPhiSeq" 

	version("0.2.0", md5="c76c0310df602f82c268cc7bf9eb9bb8")

	depends_on("r@3.1:", type=("build", "run"))
