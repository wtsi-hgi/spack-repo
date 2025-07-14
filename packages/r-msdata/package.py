# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsdata(RPackage):
	"""Various Mass Spectrometry raw data example files

	Ion Trap positive ionization mode data in mzML file format.  Subset from 500-850 m/z and 1190-1310 seconds, incl. MS2 and MS3, intensity threshold 100.000. Extracts from FTICR Apex III, m/z 400-450.  Subset of UPLC - Bruker micrOTOFq data, both mzML and mz5. LC-MSMS and MRM files from proteomics experiments. PSI mzIdentML example files for various search engines.
	"""
	
	bioc = "msdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/msdata_0.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/msdata/msdata_0.42.0.tar.gz"]

    version("0.48.0", tag="RELEASE_3_21")
	version("0.42.0", sha256="f9bb1dc20327d800807abe991ccf9b3b45a39f0b1e4cc039f21bb4f9b1fca1ca")

	depends_on("r@3.5:", type=("build", "run"))

