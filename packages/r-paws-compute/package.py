# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPawsCompute(RPackage):
	"""'Amazon Web Services' Compute Services

	Interface to 'Amazon Web Services' compute services,
    including 'Elastic Compute Cloud' ('EC2'), 'Lambda'
    functions-as-a-service, containers, batch processing, and more
    <https://aws.amazon.com/>.
	"""
	
	homepage = "https://github.com/paws-r/paws"
	cran = "paws.compute" 

	version("0.5.0", md5="47c0b5d4dcb9d96d6b16b8dba2902a17")

	depends_on("r-paws-common@0.6:", type=("build", "run"))
