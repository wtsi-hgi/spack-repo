# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrecrec(RPackage):
	"""Calculate Accurate Precision-Recall and ROC (Receiver Operator
Characteristics) Curves

	Accurate calculations and visualization of precision-recall and ROC (Receiver Operator Characteristics)
    curves. Saito and Rehmsmeier (2015) <doi:10.1371/journal.pone.0118432>.
	"""
	
	homepage = "https://github.com/evalclass/precrec"
	cran = "precrec" 

	version("0.14.4", md5="5e72bd816e62c1bc1d431bde4360a291")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-gridextra@2:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-withr@2.3:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
