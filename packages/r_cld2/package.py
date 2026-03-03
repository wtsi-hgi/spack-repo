# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCld2(RPackage):
	"""Google's Compact Language Detector 2

	Bindings to Google's C++ library Compact Language Detector 2
    (see <https://github.com/cld2owners/cld2#readme> for more information). Probabilistically
    detects over 80 languages in plain text or HTML. For mixed-language input it returns the
    top three detected languages and their approximate proportion of the total classified 
    text bytes (e.g. 80% English and 20% French out of 1000 bytes). There is also a 'cld3'
    package on CRAN which uses a neural network model instead.
	"""
	
	homepage = "https://docs.ropensci.org/cld2/"
	cran = "cld2" 

	version("1.2.4", md5="eb5750d81fad22f998c68ed077fc1c80", url="https://cran.r-project.org/src/contrib/cld2_1.2.4.tar.gz")

	depends_on("r-rcpp", type=("build", "run"))
