# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpant(RPackage):
	"""MR Spectroscopy Analysis Tools

	Tools for reading, visualising and processing Magnetic Resonance
    Spectroscopy data. The package includes methods for spectral fitting: Wilson
    (2021) <DOI:10.1002/mrm.28385> and spectral alignment: Wilson (2018)
    <DOI:10.1002/mrm.27605>. 
	"""
	
	homepage = "https://martin3141.github.io/spant/"
	cran = "spant" 

	version("2.17.0", md5="4ab737260511b3bcb7e8df6d7e526a7c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-smoother", type=("build", "run"))
	depends_on("r-ptw", type=("build", "run"))
	depends_on("r-mmand", type=("build", "run"))
	depends_on("r-rnifti", type=("build", "run"))
	depends_on("r-rniftyreg", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
