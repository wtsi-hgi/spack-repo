# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmtl(RPackage):
	"""Tools for Applying Distribution Mapping Based Transfer Learning

	
	Implementation of a transfer learning framework employing distribution mapping based domain transfer. Uses the renowned concept of histogram matching (see Gonzalez and Fittes (1977) <doi:10.1016/0094-114X(77)90062-3>, Gonzalez and Woods (2008) <isbn:9780131687288>) and extends it to include distribution measures like kernel density estimates (KDE; see Wand and Jones (1995) <isbn:978-0-412-55270-0>, Jones et al. (1996) <doi:10.2307/2291420). In the typical application scenario, one can use the underlying sample distributions (histogram or KDE) to generate a map between two distinct but related domains to transfer the target data to the source domain and utilize the available source data for better predictive modeling design. Suitable for the case where a one-to-one sample matching is not possible, thus one needs to transform the underlying data distribution to utilize the more available data for modeling. 
	"""
	
	homepage = "https://github.com/dhruba018/DMTL"
	cran = "DMTL" 

	version("0.1.2", md5="560bb35e8d541c17578bf64c19179a42")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-caret@6.0.86:", type=("build", "run"))
	depends_on("r-glmnet@4.1:", type=("build", "run"))
	depends_on("r-kernlab@0.9.29:", type=("build", "run"))
	depends_on("r-ks@1.11.7:", type=("build", "run"))
	depends_on("r-randomforest@4.6.14:", type=("build", "run"))
