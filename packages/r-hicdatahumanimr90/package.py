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

	version("1.28.0", commit="ffeee9ed45a61ce9af15fc4572a04b41b56d30e9")
	version("1.22.0", commit="594e14e3dc40c809c387e33d1757ef1846585fdf")

	depends_on("r@3.5:", type=("build", "run"))

