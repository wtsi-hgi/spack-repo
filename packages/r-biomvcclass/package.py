# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiomvcclass(RPackage):
	"""Model-View-Controller (MVC) Classes That Use Biobase

	Creates classes used in model-view-controller (MVC) design
	"""
	
	bioc = "BioMVCClass" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BioMVCClass_1.70.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BioMVCClass/BioMVCClass_1.70.0.tar.gz"]

    version("1.76.0", tag="RELEASE_3_21")
	version("1.70.0", sha256="ddf12f5b1c2bc2d16833be0257d98e407b5fed5d0b58bb1b685ce1587cd89311")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-mvcclass", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
