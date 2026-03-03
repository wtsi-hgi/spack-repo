# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPawsEndUserComputing(RPackage):
	"""'Amazon Web Services' End User Computing Services

	Interface to 'Amazon Web Services' end user computing
    services, including collaborative document editing, mobile intranet,
    and more <https://aws.amazon.com/>.
	"""
	
	homepage = "https://github.com/paws-r/paws"
	cran = "paws.end.user.computing" 

	version("0.5.0", md5="8307a80d3a6d92f2ac3cab8171e25e52")

	depends_on("r-paws-common@0.6:", type=("build", "run"))
