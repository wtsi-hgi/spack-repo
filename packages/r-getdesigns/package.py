# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetdesigns(RPackage):
	"""Generalized Extended Triangular Designs ('GETdesigns')

	Since their introduction by Bose and Nair (1939) <https://www.jstor.org/stable/40383923>, partially balanced incomplete block (PBIB) designs remain an important class of incomplete block designs. The concept of association scheme was used by Bose and Shimamoto (1952) <doi:10.1080/01621459.1952.10501161> for the classification of these designs. The constraint of resources always motivates the experimenter to advance towards PBIB designs, more specifically to higher associate class PBIB designs from balanced incomplete block designs. It is interesting to note that many times higher associate PBIB designs perform better than their counterpart lower associate PBIB designs for the same set of parameters v, b, r, k and lambda_i (i=1,2...m). This package contains functions named GETD() for generating m-associate (m>=2) class PBIB designs along with parameters (v, b, r, k and lambda_i, i = 1, 2,…,m) based on Generalized Triangular (GT) Association Scheme. It also calculates the Information matrix, Average variance factor and canonical efficiency factor of the generated design. These designs, besides having good efficiency, require smaller number of replications and smallest possible concurrence of treatment pairs.
	"""
	
	cran = "GETdesigns" 

	version("1.2.0", md5="c18ca14b0ae95d7106ab310401f1bff6")
	version("1.1.0", md5="f77d8c791b55830ff70085d3dd96fd48")

