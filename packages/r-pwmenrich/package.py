# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwmenrich(RPackage):
	"""PWM enrichment analysis

	A toolkit of high-level functions for DNA motif scanning and enrichment analysis built upon Biostrings. The main functionality is PWM enrichment analysis of already known PWMs (e.g. from databases such as MotifDb), but the package also implements high-level functions for PWM scanning and visualisation. The package does not perform "de novo" motif discovery, but is instead focused on using motifs that are either experimentally derived or computationally constructed by other tools.
	"""
	
	bioc = "PWMEnrich" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PWMEnrich_4.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PWMEnrich/PWMEnrich_4.38.0.tar.gz"]

	version("4.38.0", md5="ced56cbfbab381f5736f4f58fe26b9f8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-seqlogo", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
