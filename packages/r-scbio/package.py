# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScbio(RPackage):
	"""Single Cell Genomics for Enhancing Cell Composition Inference
from Bulk Genomics Data

	Cellular population mapping (CPM) a deconvolution algorithm in which single-cell genomics is required in only one or a few samples, where in other samples of the same tissue, only bulk genomics is measured and the underlying fine resolution cellular heterogeneity is inferred.
	"""
	
	homepage = "https://github.com/amitfrish/scBio"
	cran = "scBio" 

	version("0.1.6", md5="ffeaa5a6de180c86dd63c2eec0c09269")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-liblinear", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
