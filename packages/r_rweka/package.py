# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRweka(RPackage):
	"""R/Weka Interface

	An R interface to Weka (Version 3.9.3).
   Weka is a collection of machine learning algorithms for data mining
   tasks written in Java, containing tools for data pre-processing,
   classification, regression, clustering, association rules, and
   visualization.  Package 'RWeka' contains the interface code, the
   Weka jar is in a separate package 'RWekajars'.  For more information
   on Weka see <https://www.cs.waikato.ac.nz/ml/weka/>.
	"""
	
	cran = "RWeka" 

	version("0.4-46", md5="fb85348c2dcd57210d4aad9d68bfceb7")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-rwekajars@3.9.3.1:", type=("build", "run"))
	depends_on("r-rjava@0.6.3:", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
