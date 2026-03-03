# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScina(RPackage):
	"""A Semi-Supervised Category Identification and Assignment Tool

	An automatic cell type detection and assignment algorithm for single cell RNA-Seq and Cytof/FACS data. 'SCINA' is capable of assigning cell type identities to a pool of cells profiled by scRNA-Seq or Cytof/FACS data with prior knowledge of markers, such as genes and protein symbols that are highly or lowly expressed in each category. See Zhang Z, et al (2019) <doi:10.3390/genes10070531> for more details.
	"""
	
	homepage = "http://lce.biohpc.swmed.edu/scina/"
	cran = "SCINA" 

	version("1.2.0", md5="6ba993e1dff739b7741990621b2f9f48")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
