# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRucrdtw(RPackage):
	"""R Bindings for the UCR Suite

	R bindings for functions from the UCR Suite by Rakthanmanon et al. (2012) <DOI:10.1145/2339530.2339576>, which enables ultrafast subsequence
      search for a best match under Dynamic Time Warping and Euclidean Distance.
	"""
	
	homepage = "https://github.com/pboesu/rucrdtw"
	cran = "rucrdtw" 

	version("0.1.6", md5="4aaf9e9488578caf16fe4f6f75772c05")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
