# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPawsNetworking(RPackage):
	"""'Amazon Web Services' Networking & Content Delivery Services

	Interface to 'Amazon Web Services' networking and content
    delivery services, including 'Route 53' Domain Name System service,
    'CloudFront' content delivery, load balancing, and more
    <https://aws.amazon.com/>.
	"""
	
	homepage = "https://github.com/paws-r/paws"
	cran = "paws.networking" 

	version("0.5.0", md5="12396cc580b968f8b6cebb15ae649d09")

	depends_on("r-paws-common@0.6:", type=("build", "run"))
