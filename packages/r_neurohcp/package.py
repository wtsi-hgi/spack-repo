# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeurohcp(RPackage):
	"""Human 'Connectome' Project Interface

	Downloads and reads data from Human 'Connectome' Project 
    <https://db.humanconnectome.org> using Amazon Web Services ('AWS') 
    'S3' buckets.
	"""
	
	homepage = "https://db.humanconnectome.org"
	cran = "neurohcp" 

	version("0.9.0", md5="e52b04f7122a43e44aa830b675e5c375")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml2@1.0.1:", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-aws-s3", type=("build", "run"))
