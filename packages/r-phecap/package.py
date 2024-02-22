# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhecap(RPackage):
	"""High-Throughput Phenotyping with EHR using a Common Automated
Pipeline

	Implement surrogate-assisted feature extraction (SAFE) and
             common machine learning approaches to train and validate phenotyping models.
             Background and details about the methods can be found at 
             Zhang et al. (2019) <doi:10.1038/s41596-019-0227-6>,
             Yu et al. (2017) <doi:10.1093/jamia/ocw135>, and 
             Liao et al. (2015) <doi:10.1136/bmj.h1885>.
	"""
	
	homepage = "https://celehs.github.io/PheCAP/"
	cran = "PheCAP" 

	version("1.2.1", md5="b69e390eb647c4f47d8b7df1fa1ec800")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rmysql", type=("build", "run"))
