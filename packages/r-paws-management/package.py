# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPawsManagement(RPackage):
	"""'Amazon Web Services' Management & Governance Services

	Interface to 'Amazon Web Services' management and governance
    services, including 'CloudWatch' application and infrastructure
    monitoring, 'Auto Scaling' for automatically scaling resources, and
    more <https://aws.amazon.com/>.
	"""
	
	homepage = "https://github.com/paws-r/paws"
	cran = "paws.management" 

	version("0.5.0", md5="77e879d8ac276aeb2071aad131c8e210")

	depends_on("r-paws-common@0.6:", type=("build", "run"))
