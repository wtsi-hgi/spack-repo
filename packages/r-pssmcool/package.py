# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPssmcool(RPackage):
	"""Features Extracted from Position Specific Scoring Matrix (PSSM)

	Returns almost all features that has been extracted from Position Specific 
             Scoring Matrix (PSSM) so far, which is a matrix of L rows (L is protein length) 
             and 20 columns produced by 'PSI-BLAST' which is a program to produce
             PSSM Matrix from multiple sequence alignment of proteins
             see <https://www.ncbi.nlm.nih.gov/books/NBK2590/> for mor details. some 
             of these features are described in Zahiri, J., et al.(2013)
             <DOI:10.1016/j.ygeno.2013.05.006>,
             Saini, H., et al.(2016)
             <DOI:10.17706/jsw.11.8.756-767>,
             Ding, S., et al.(2014)
             <DOI:10.1016/j.biochi.2013.09.013>,
             Cheng, C.W., et al.(2008)
             <DOI:10.1186/1471-2105-9-S12-S6>,
             Juan, E.Y., et al.(2009)
             <DOI:10.1109/CISIS.2009.194>. 
	"""
	
	homepage = "https://github.com/BioCool-Lab/PSSMCOOL"
	cran = "PSSMCOOL" 

	version("0.2.4", md5="177259d6bcefd46b41cce9adae8c2bcc")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
	depends_on("r-phontools", type=("build", "run"))
	depends_on("r-dtt", type=("build", "run"))
