# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImpimp(RPackage):
	"""Imprecise Imputation for Statistical Matching

	Imputing blockwise missing data by imprecise imputation,
    featuring a domain-based, variable-wise, and case-wise strategy. 
    Furthermore, the estimation of lower and upper bounds for 
    unconditional and conditional probabilities based on the obtained
    imprecise data is implemented.
    Additionally, two utility functions are supplied: one to check 
    whether variables in a data set contain set-valued observations;
    and another to merge two already imprecisely imputed data. 
    The method is described in a technical report by Endres, Fink and
    Augustin (2018, <doi:10.5282/ubm/epub.42423>).
	"""
	
	cran = "impimp" 

	version("0.3.1", md5="8422843174f0a6c9c185fb7316216a72")

