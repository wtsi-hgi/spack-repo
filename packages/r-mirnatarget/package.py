# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirnatarget(RPackage):
	"""gene target tabale of miRNA for human/mouse used for MiRaGE package

	gene target tabale of miRNA for human/mouse used for MiRaGE package
	"""
	
	bioc = "miRNATarget" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/miRNATarget_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/miRNATarget/miRNATarget_1.40.0.tar.gz"]

	version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="1ef4bf4e9f7e75417c7e3aa818d379ff6f421cfaf36201d70391a7aceafd8a62")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

