# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFile2meco(RPackage):
	"""Transform Files to 'microtable' Object with 'microeco' Package

	Transform output files of some tools to the 'microtable' object of 'microtable' class in 'microeco' package. The 'microtable' class is the basic class in 'microeco' package and is necessary for the downstream microbial community data analysis.
	"""
	
	homepage = "https://github.com/ChiLiubio/file2meco"
	cran = "file2meco" 

	version("0.7.1", md5="0de63809afc5e870af64cf6c389c9ccc")
	version("0.7.0", md5="71fb2f093b015915f03b40ab4cd15b17")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-microeco@1.2:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
