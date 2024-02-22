# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlmm(RPackage):
	"""A Genotype Calling Algorithm for Affymetrix SNP Arrays

	A classification algorithm, based on a multi-chip, multi-SNP approach for Affymetrix SNP arrays. Using a large training sample where the genotype labels are known, this aglorithm will obtain more accurate classification results on new data. RLMM is based on a robust, linear model and uses the Mahalanobis distance for classification. The chip-to-chip non-biological variation is removed through normalization. This model-based algorithm captures the similarities across genotype groups and probes, as well as thousands other SNPs for accurate classification. NOTE: 100K-Xba only at for now.
	"""
	
	homepage = "http://www.stat.berkeley.edu/users/nrabbee/RLMM"
	bioc = "RLMM" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/RLMM_1.64.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/RLMM/RLMM_1.64.0.tar.gz"]

	version("1.64.0", md5="7c43c967fab2a5e90059b26e46de345b")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
