# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGina(RPackage):
	"""High Throughput Phenotyping

	Performs image segmentation in fruit or seeds pictures in order to measure physical features in a high-throughput manner for genome-wide association (GWAS) and genomic selection programs.
	"""
	
	homepage = "http://www.wisc.edu"
	cran = "GiNA" 

	version("1.0.1", md5="19ed8ae5e248d38ef11a258cf5123b69")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
