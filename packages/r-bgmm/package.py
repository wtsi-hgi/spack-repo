# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgmm(RPackage):
	"""Gaussian Mixture Modeling Algorithms and the Belief-Based
Mixture Modeling

	Two partially supervised mixture modeling methods: 
        soft-label and belief-based modeling are implemented.
        For completeness, we equipped the package also with the
        functionality of unsupervised, semi- and fully supervised
        mixture modeling.  The package can be applied also to selection
        of the best-fitting from a set of models with different
        component numbers or constraints on their structures.
        For detailed introduction see:
        Przemyslaw Biecek, Ewa Szczurek, Martin Vingron, Jerzy
        Tiuryn (2012), The R Package bgmm: Mixture Modeling with
        Uncertain Knowledge, Journal of Statistical Software 
        <doi:10.18637/jss.v047.i03>.
	"""
	
	homepage = "http://bgmm.molgen.mpg.de/"
	cran = "bgmm" 

	version("1.8.5", md5="8519cdbda534e70809a905f5c01ef90f")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
