# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmtdata(RPackage):
	"""An ExperimentHub Package for data sets with an Epithelial to Mesenchymal Transition (EMT)

	This package provides pre-processed RNA-seq data where the epithelial to mesenchymal transition was induced on cell lines. These data come from three publications Cursons et al. (2015), Cursons etl al. (2018) and Foroutan et al. (2017). In each of these publications, EMT was induces across multiple cell lines following treatment by TGFb among other stimulants. This data will be useful in determining the regulatory programs modified in order to achieve an EMT. Data were processed by the Davis laboratory in the Bioinformatics division at WEHI.
	"""
	
	homepage = "https://github.com/DavisLaboratory/emtdata"
	bioc = "emtdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/emtdata_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/emtdata/emtdata_1.10.0.tar.gz"]

	version("1.10.0", md5="4f861584cce979edd6d7bdce3624e916")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

