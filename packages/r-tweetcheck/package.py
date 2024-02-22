# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTweetcheck(RPackage):
	"""Parse and Validate Tweet Text

	An interface to 'twitter-text', a 'JavaScript' library which
   is responsible for determining the length/validity of a tweet and 
   identifying/linking any URLs or special tags (e.g. mentions or
   hashtags) which may be present.
	"""
	
	cran = "tweetcheck" 

	version("0.1.0", md5="1efae8b5ad471261323644ed8316a702")

	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
