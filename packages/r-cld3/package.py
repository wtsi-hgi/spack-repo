# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCld3(RPackage):
	"""Google's Compact Language Detector 3

	Google's Compact Language Detector 3 is a neural network model for language 
    identification and the successor of 'cld2' (available from CRAN). The algorithm is still
    experimental and takes a novel approach to language detection with different properties
    and outcomes. It can be useful to combine this with the Bayesian classifier results 
    from 'cld2'. See <https://github.com/google/cld3#readme> for more information.
	"""
	
	homepage = "https://docs.ropensci.org/cld3/"
	cran = "cld3" 

	version("1.6.0", md5="be77a3493aea78479ef7461fe1108267", url="https://cran.r-project.org/src/contrib/cld3_1.6.0.tar.gz")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("protobuf", type=("build", "link", "run"))
