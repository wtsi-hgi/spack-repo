# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLtable(RPackage):
	"""Easy to Make (Lazy) Tables

	Constructs tables of counts and proportions out of data sets with possibility to insert tables to Excel, Word, HTML, and PDF documents. Transforms tables to data suitable for modelling. Features Gibbs sampling based log-linear (NB2) and power analyses (original by Oleksandr Ocheredko <doi:10.35566/isdsa2019c5>) for tabulated data.  
	"""
	
	cran = "ltable" 

	version("2.0.3", md5="ecd00f2c04088ce68392b8739f75700c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
