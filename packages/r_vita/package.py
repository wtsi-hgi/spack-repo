# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVita(RPackage):
	"""Variable Importance Testing Approaches

	Implements the novel testing approach by Janitza et al.(2015)
    <http://nbn-resolving.de/urn/resolver.pl?urn=nbn:de:bvb:19-epub-25587-4>
    for the permutation variable importance measure in a random forest and the
    PIMP-algorithm by Altmann et al.(2010) <doi:10.1093/bioinformatics/btq134>.
    Janitza et al.(2015) <http://nbn-resolving.de/urn/resolver.pl?urn=nbn:de:bvb:19-epub-25587-4>
    do not use the "standard" permutation variable
    importance but the cross-validated permutation variable
    importance for the novel test approach. The cross-validated
    permutation variable importance is not based on the out-of-bag
    observations but uses a similar strategy which is inspired by
    the cross-validation procedure. The novel test approach can be
    applied for classification trees as well as for regression
    trees. However, the use of the novel testing approach has not
    been tested for regression trees so far, so this routine is
    meant for the expert user only and its current state is rather
    experimental.
	"""
	
	cran = "vita" 

	version("1.0.0", md5="a18e6b529e669c8cdd5bf41ae8d255e3")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
