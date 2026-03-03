# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdam(RPackage):
	"""Social Dynamics and Complexity in the Ancient Mediterranean

	Provides digital tools for performing analyses within Social Dynamics and complexity in the Ancient Mediterranean (SDAM), which is a research group based at the Department of History and Classical Studies at Aarhus University. 
	"""
	
	homepage = "https://github.com/sdam-au/sdam/"
	cran = "sdam" 

	version("1.1.4", md5="812a56956f0904644981a8e07a8a47c5")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-grimport2", type=("build", "run"))
	depends_on("r-multiplex", type=("build", "run"))
