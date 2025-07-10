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

	version("1.76.0", sha256="5d5d37965e01b685cb666a0e487723ed685faebb70862d70e9c62684cdb5d199")

	depends_on("r@2.1:", type=("build", "run"))
