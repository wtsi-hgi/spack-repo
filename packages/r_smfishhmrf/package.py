# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmfishhmrf(RPackage):
	"""Hidden Markov Random Field for Spatial Transcriptomic Data

	Discovery of spatial patterns with Hidden Markov Random Field. This package is designed for spatial transcriptomic data and single molecule fluorescent in situ hybridization (FISH) data such as sequential fluorescence in situ hybridization (seqFISH) and multiplexed error-robust fluorescence in situ hybridization (MERFISH). The methods implemented in this package are described in Zhu et al. (2018) <doi:10.1038/nbt.4260>.
	"""
	
	homepage = "https://bitbucket.org/qzhudfci/smfishhmrf-r/src/master/"
	cran = "smfishHmrf" 

	version("0.1", md5="9f9897e2f27ef89d9752de831ede87e1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pracma@1.9:", type=("build", "run"))
	depends_on("r-fs@1.2:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
