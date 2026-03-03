# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPawsCustomerEngagement(RPackage):
	"""'Amazon Web Services' Customer Engagement Services

	Interface to 'Amazon Web Services' customer engagement
    services, including 'Simple Email Service', 'Connect' contact center
    service, and more <https://aws.amazon.com/>.
	"""
	
	homepage = "https://github.com/paws-r/paws"
	cran = "paws.customer.engagement" 

	version("0.5.0", md5="cace71f2b5bddc24a8a3a2c28b3f13fb")

	depends_on("r-paws-common@0.6:", type=("build", "run"))
