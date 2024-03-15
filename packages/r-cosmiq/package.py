# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCosmiq(RPackage):
	"""cosmiq - COmbining Single Masses Into Quantities

	cosmiq is a tool for the preprocessing of liquid- or gas - chromatography mass spectrometry (LCMS/GCMS) data with a focus on metabolomics or lipidomics applications. To improve the detection of low abundant signals, cosmiq generates master maps of the mZ/RT space from all acquired runs before a peak detection algorithm is applied. The result is a more robust identification and quantification of low-intensity MS signals compared to conventional approaches where peak picking is performed in each LCMS/GCMS file separately. The cosmiq package builds on the xcmsSet object structure and can be therefore integrated well with the package xcms as an alternative preprocessing step.
	"""
	
	homepage = "http://www.bioconductor.org/packages/devel/bioc/html/cosmiq.html"
	bioc = "cosmiq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cosmiq_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cosmiq/cosmiq_1.36.0.tar.gz"]

	version("1.36.0", md5="ae02870f3759e09bb2c8f86d38306f01")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-xcms", type=("build", "run"))
	depends_on("r-massspecwavelet", type=("build", "run"))
	depends_on("r-faahko", type=("build", "run"))
