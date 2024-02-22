# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPawsStorage(RPackage):
	"""'Amazon Web Services' Storage Services

	Interface to 'Amazon Web Services' storage services,
    including 'Simple Storage Service' ('S3') and more
    <https://aws.amazon.com/>.
	"""
	
	homepage = "https://github.com/paws-r/paws"
	cran = "paws.storage" 

	version("0.5.0", md5="c346325ae9e1716359ddc85eed341412")

	depends_on("r-paws-common@0.6:", type=("build", "run"))
