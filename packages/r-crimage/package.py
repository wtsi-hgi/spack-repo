# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrimage(RPackage):
	"""CRImage a package to classify cells and calculate tumour cellularity

	CRImage provides functionality to process and analyze images, in particular to classify cells in biological images. Furthermore, in the context of tumor images, it provides functionality to calculate tumour cellularity.
	"""
	
	bioc = "CRImage" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CRImage_1.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CRImage/CRImage_1.50.0.tar.gz"]

    version("1.56.0", tag="RELEASE_3_21")
	version("1.50.0", sha256="2c76f9b6442da822ce054f6fb86f032644974e7d420aa4512c5e1b6a163d747b")

	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
	depends_on("r-acgh", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-sgeostat", type=("build", "run"))
