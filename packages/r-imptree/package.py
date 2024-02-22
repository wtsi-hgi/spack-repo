# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImptree(RPackage):
	"""Classification Trees with Imprecise Probabilities

	Creation of imprecise classification trees. They rely on
    probability estimation within each node by means of either the
    imprecise Dirichlet model or the nonparametric predictive
    inference approach. The splitting variable is selected by the
    strategy presented in Fink and Crossman (2013)
    <http://www.sipta.org/isipta13/index.php?id=paper&paper=014.html>,
    but also the original imprecise information gain of Abellan and
    Moral (2003) <doi:10.1002/int.10143> is covered.
	"""
	
	cran = "imptree" 

	version("0.5.1", md5="be86fe7e25f81ae1d95394f66f261c8f")

	depends_on("r-rcpp", type=("build", "run"))
