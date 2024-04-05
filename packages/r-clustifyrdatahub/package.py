# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustifyrdatahub(RPackage):
	"""External data sets for clustifyr in ExperimentHub

	References made from external single-cell mRNA sequencing data sets, stored as average gene expression matrices. For use with clustifyr <https://bioconductor.org/packages/clustifyr> to assign cell type identities.
	"""
	
	homepage = "https://rnabioco.github.io/clustifyrdatahub/"
	bioc = "clustifyrdatahub" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/clustifyrdatahub_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/clustifyrdatahub/clustifyrdatahub_1.12.0.tar.gz"]

	version("1.12.0", md5="aac4529e5c0d71fdc49bda51c3915f61")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

