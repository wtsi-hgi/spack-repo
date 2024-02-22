# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPawsCostManagement(RPackage):
	"""'Amazon Web Services' Cost Management Services

	Interface to 'Amazon Web Services' cost management services,
    including cost and usage reports, budgets, pricing, and more
    <https://aws.amazon.com/>.
	"""
	
	homepage = "https://github.com/paws-r/paws"
	cran = "paws.cost.management" 

	version("0.5.0", md5="7778014571fe950b98817e7041002125")

	depends_on("r-paws-common@0.6:", type=("build", "run"))
