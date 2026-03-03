# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcalignr(RPackage):
	"""Simple Peak Alignment for Gas-Chromatography Data

	Aligns peak based on peak retention times and matches homologous peaks
    across samples. The underlying alignment procedure comprises three sequential steps.
    (1) Full alignment of samples by linear transformation of retention times to 
    maximise similarity among homologous peaks (2) Partial alignment of peaks within 
    a user-defined retention time window to cluster homologous peaks (3) Merging rows
    that are likely representing homologous substances (i.e. no sample shows peaks in 
    both rows and the rows have similar retention time means). The algorithm is described in detail
    in Ottensmann et al., 2018 <doi:10.1371/journal.pone.0198311>. 
	"""
	
	homepage = "https://github.com/mottensmann/GCalignR"
	cran = "GCalignR" 

	version("1.0.6", md5="c1f3a2ce0ac3e67d1821da5b75cf8220")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
