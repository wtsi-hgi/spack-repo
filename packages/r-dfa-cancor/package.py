# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfaCancor(RPackage):
	"""Linear Discriminant Function and Canonical Correlation Analysis

	
  Produces SPSS- and SAS-like output for linear discriminant 
  function analysis and canonical correlation analysis. The methods are described in
  Manly & Alberto (2017, ISBN:9781498728966),
  Rencher (2002, ISBN:0-471-41889-7), and
  Tabachnik & Fidell (2019, ISBN:9780134790541).
	"""
	
	cran = "DFA.CANCOR" 

	version("0.2.8", md5="f63a5d931a38f0affb19ef6c6e3450a3")

	depends_on("r-bayesfactor", type=("build", "run"))
	depends_on("r-mvn", type=("build", "run"))
