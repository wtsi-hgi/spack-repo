# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPawsApplicationIntegration(RPackage):
	"""'Amazon Web Services' Application Integration Services

	Interface to 'Amazon Web Services' application integration
    services, including 'Simple Queue Service' ('SQS') message queue,
    'Simple Notification Service' ('SNS') publish/subscribe messaging, and
    more <https://aws.amazon.com/>.
	"""
	
	homepage = "https://github.com/paws-r/paws"
	cran = "paws.application.integration" 

	version("0.5.0", md5="55fca4015badf438e9d98227da248c20")

	depends_on("r-paws-common@0.6:", type=("build", "run"))
