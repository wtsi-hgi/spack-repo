# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasierdata(RPackage):
	"""easier internal data and exemplary dataset from IMvigor210CoreBiologies package

	Access to internal data required for the functional performance of easier package and exemplary bladder cancer dataset with both processed RNA-seq data and information on response to ICB therapy generated by Mariathasan et al. "TGF-B attenuates tumour response to PD-L1 blockade by contributing to exclusion of T cells", published in Nature, 2018 [doi:10.1038/nature25501](https://doi.org/10.1038/nature25501). The data is made available via [`IMvigor210CoreBiologies`](http://research-pub.gene.com/IMvigor210CoreBiologies/) package under the CC-BY license.
	"""
	
	bioc = "easierData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/easierData_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/easierData/easierData_1.8.0.tar.gz"]

	version("1.8.0", md5="5092649863b833021ff8593731571183")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

	# experiment