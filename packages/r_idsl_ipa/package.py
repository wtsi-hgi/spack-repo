# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdslIpa(RPackage):
	"""Intrinsic Peak Analysis (IPA) for HRMS Data

	A multi-layered untargeted pipeline for high-throughput LC/HRMS data processing to extract signals of organic small molecules. The package performs ion pairing, peak detection, peak table alignment, retention time correction, aligned peak table gap filling, peak annotation and visualization of extracted ion chromatograms (EICs) and total ion chromatograms (TICs). The 'IDSL.IPA' package was introduced in <doi:10.1021/acs.jproteome.2c00120> .
	"""
	
	homepage = "https://github.com/idslme/idsl.ipa"
	cran = "IDSL.IPA" 

	version("2.9", md5="f538e45ca623116399761cbb5eb76f49")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-idsl-mxp", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
