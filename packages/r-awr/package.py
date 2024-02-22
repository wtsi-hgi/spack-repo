# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwr(RPackage):
	"""'AWS' Java 'SDK' for R

	Make the compiled Java modules of the Amazon Web Services ('AWS') 'SDK' available to be used in downstream R packages interacting with 'AWS'. See <https://aws.amazon.com/sdk-for-java> for more information on the 'AWS' 'SDK' for Java.
	"""
	
	homepage = "https://github.com/daroczig/AWR"
	cran = "AWR" 

	version("1.11.189-1", md5="6e129e6d8dff23c41a306c61f8f706c9")

	depends_on("r-rjava", type=("build", "run"))
