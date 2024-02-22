# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRibd(RPackage):
	"""Pedigree-based Relatedness Coefficients

	Recursive algorithms for computing various relatedness
    coefficients, including pairwise kinship, kappa and identity
    coefficients. Both autosomal and X-linked coefficients are computed.
    Founders are allowed to be inbred, which enables construction of any
    given kappa coefficients, as described in Vigeland (2020)
    <doi:10.1007/s00285-020-01505-x>. In addition to the standard
    coefficients, 'ribd' also computes a range of lesser-known
    coefficients, including generalised kinship coefficients (Karigl
    (1981) <doi:10.1111/j.1469-1809.1981.tb00341.x>; Weeks and Lange
    (1988) <https://pubmed.ncbi.nlm.nih.gov/3422543/>),
    two-locus coefficients (Thompson (1988) <doi:10.1093/imammb/5.4.261>)
    and multi-person coefficients. Many features of 'ribd' are available
    through the online app 'QuickPed' at
    <https://magnusdv.shinyapps.io/quickped>; see Vigeland (2022)
    <doi:10.1186/s12859-022-04759-y>.
	"""
	
	homepage = "https://github.com/magnusdv/ribd"
	cran = "ribd" 

	version("1.6.1", md5="b1fa2ed7b11224bc886e762a4a58d8cb")

	depends_on("r-pedtools@2:", type=("build", "run"))
	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-kinship2", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
