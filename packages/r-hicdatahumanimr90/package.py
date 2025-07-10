# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHicdatahumanimr90(RPackage):
	"""Human IMR90 Fibroblast HiC data from Dixon et al. 2012

	The HiC data from Human Fibroblast IMR90 cell line (HindIII restriction) was retrieved from the GEO website, accession number GSE35156 (http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE35156). The raw reads were processed as explained in Dixon et al. (Nature 2012).
	"""
	
	bioc = "HiCDataHumanIMR90" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/HiCDataHumanIMR90_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/HiCDataHumanIMR90/HiCDataHumanIMR90_1.22.0.tar.gz"]

	version("1.22.0", sha256="3df6a6c98f3d83c9079ab913bf6c0e1fa069248674c7e1fd1071b68df085c5cb", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/HiCDataHumanIMR90_1.22.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))

