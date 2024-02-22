# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParan(RPackage):
	"""Horn's Test of Principal Components/Factors

	An implementation of Horn's technique for numerically and graphically evaluating the components or factors retained in a principle components analysis (PCA) or common factor analysis (FA). Horn's method contrasts eigenvalues produced through a PCA or FA on a number of random data sets of uncorrelated variables with the same number of variables and observations as the experimental or observational data set to produce eigenvalues for components or factors that are adjusted for the sample error-induced inflation. Components with adjusted eigenvalues greater than one are retained. paran may also be used to conduct parallel analysis following Glorfeld's (1995) suggestions to reduce the likelihood of over-retention.
	"""
	
	homepage = "http://alexisdinno.com/Software/files/PA_for_PCA_vs_FA.pdf"
	cran = "paran" 

	version("1.5.2", md5="b9ab6c3acc8fcf3ff0206ebffcd208ad")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
