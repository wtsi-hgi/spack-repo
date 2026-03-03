# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPawsSecurityIdentity(RPackage):
	"""'Amazon Web Services' Security, Identity, & Compliance Services

	Interface to 'Amazon Web Services' security, identity, and
    compliance services, including the 'Identity & Access Management'
    ('IAM') service for managing access to services and resources, and
    more <https://aws.amazon.com/>.
	"""
	
	homepage = "https://github.com/paws-r/paws"
	cran = "paws.security.identity" 

	version("0.5.0", md5="321c597179913b5e1911ef1e36ce6891")

	depends_on("r-paws-common@0.6:", type=("build", "run"))
