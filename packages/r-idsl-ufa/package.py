# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdslUfa(RPackage):
	"""United Formula Annotation (UFA) for HRMS Data Processing

	A pipeline to annotate chromatography peaks from the 'IDSL.IPA' workflow <doi:10.1021/acs.jproteome.2c00120> with molecular formulas of a prioritized chemical space using an isotopic profile matching approach. The 'IDSL.UFA' workflow only requires mass spectrometry level 1 (MS1) data for formula annotation. The 'IDSL.UFA' methods was described in <doi:10.1021/acs.analchem.2c00563> .
	"""
	
	homepage = "https://github.com/idslme/idsl.ufa"
	cran = "IDSL.UFA" 

	version("2.0", md5="a2d0800694689b3fca855990295be684")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-idsl-ipa@2.7:", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
