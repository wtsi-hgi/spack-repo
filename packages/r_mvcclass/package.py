# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvcclass(RPackage):
	"""Model-View-Controller (MVC) Classes

	Creates classes used in model-view-controller (MVC) design
	"""
	
	bioc = "MVCClass" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MVCClass_1.76.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MVCClass/MVCClass_1.76.0.tar.gz"]

	version("1.76.0", md5="2ef3331b86ae7981a2ab3323386caf61")

	depends_on("r@2.1:", type=("build", "run"))
