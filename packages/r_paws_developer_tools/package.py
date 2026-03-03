# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPawsDeveloperTools(RPackage):
	"""'Amazon Web Services' Developer Tools Services

	Interface to 'Amazon Web Services' developer tools services,
    including version control, continuous integration and deployment, and
    more <https://aws.amazon.com/products/developer-tools/>.
	"""
	
	homepage = "https://github.com/paws-r/paws"
	cran = "paws.developer.tools" 

	version("0.5.0", md5="c9934855decd54e82f9394ec5a9a5604")

	depends_on("r-paws-common@0.6:", type=("build", "run"))
