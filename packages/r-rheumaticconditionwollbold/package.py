# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRheumaticconditionwollbold(RPackage):
	"""Normalized gene expression dataset published by Wollbold et al. [2009] (WOLLBOLD).

	Normalized gene expression data from rheumatic diseases from study published by Wollbold et al. in 2009, provided as an eSet.
	"""
	
	homepage = "http://compbio.dfci.harvard.edu/"
	bioc = "rheumaticConditionWOLLBOLD" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/rheumaticConditionWOLLBOLD_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/rheumaticConditionWOLLBOLD/rheumaticConditionWOLLBOLD_1.40.0.tar.gz"]

	version("1.40.0", md5="8c8a5f56b923fe79c4a4902028d6fc5c")

	depends_on("r@2.10:", type=("build", "run"))

	# experiment