# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntegirty(RPackage):
	"""Integrating Multiple Modalities of High Throughput Assays Using
Item Response Theory

	Provides a systematic framework for
 integrating multiple modalities of assays profiled on the same set of
 samples. The goal is to identify genes that are altered in cancer
 either marginally or consistently across different assays. The
 heterogeneity among different platforms and different samples are
 automatically adjusted so that the overall alteration magnitude can
 be accurately inferred. See Tong and Coombes (2012) 
 <doi:10.1093/bioinformatics/bts561>. 
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "integIRTy" 

	version("1.0.7", md5="64d7493119c00ee34f6b91ab4f559811")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ltm", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
