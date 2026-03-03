# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGese(RPackage):
	"""Gene-Based Segregation Test

	Implements the gene-based segregation test(GESE) and the weighted GESE test for identifying genes with causal variants of large effects for family-based sequencing data. The methods are described in Qiao, D. Lange, C., Laird, N.M., Won, S., Hersh, C.P., et al. (2017). <DOI:10.1002/gepi.22037>. Gene-based segregation method for identifying rare variants for family-based sequencing studies. Genet Epidemiol 41(4):309-319. More details can be found at <http://scholar.harvard.edu/dqiao/gese>.
	"""
	
	cran = "GESE" 

	version("2.0.1", md5="64184b4f595584afcd02130fcda18aa8")

	depends_on("r-kinship2", type=("build", "run"))
